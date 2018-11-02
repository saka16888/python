

# setenv LD_LIBRARY_PATH /csaf_auto/ats5.3.0/lib
# setenv AUTOTEST /csaf_auto/ats5.3.0
# setenv ATS_EASY /csaf_auto/ats5.3.0/ats_easy

import os
import re
import time
import logging
from ats import topology
from ats import aetest
LOGGER = logging.getLogger(__name__)

class tc_one(aetest.Testcase):
    @aetest.setup
    def setup(self):
        testbedfile = self.script_args['testbed_file']
        testbed = topology.loader.load(testbedfile)
        asa = testbed.devices['pyats-asa-28']
        asa.connect()

        asa_base_config = """
            interface GigabitEthernet0/0
             nameif inside
             security-level 100
             ip address 10.0.0.1 255.255.255.0
             no shut
            interface GigabitEthernet0/1
             nameif outside
             security-level 0
             ip address 10.0.1.1 255.255.255.0
             no shut
            object network host-10.0.0.2
             host 10.0.0.2
            object network natted-pool
             range 10.0.1.11 10.0.1.20
            object network host-10.0.0.2
             nat (any,any) dynamic natted-pool
            access-list any permit ip any any
            access-group any in interface outside
        """
        asa.config(asa_base_config)

        ubuntu1 = testbed.devices['pyats-ubuntu-1']
        ubuntu1.connect()
        ubuntu1.execute("sudo ifconfig eth1 10.0.0.2 netmask 255.255.255.0")
        ubuntu1.execute("sudo route add -net 10.0.1.0 netmask 255.255.255.0 gw 10.0.0.1")
        ubuntu2 = testbed.devices['pyats-ubuntu-2']
        ubuntu2.connect()
        ubuntu2.execute("sudo ifconfig eth1 10.0.1.2 netmask 255.255.255.0")

        self.asa = asa
        self.ubuntu1 = ubuntu1
        self.ubuntu2 = ubuntu2

    @aetest.test
    def ping_test(self):
        output = self.ubuntu1.execute("ping -c 3 10.0.0.2")
        assert "0% packet loss" in output, "output: %s" % output


    @aetest.cleanup
    def cleanup(self):
        asa_cleanup_config = """
            clear config nat
            clear config object
            clear config access-group
            clear config access-list
            clear config interface g0/0
            clear config interface g0/1
        """
        self.asa.config(asa_cleanup_config)
        self.asa.disconnect()

        self.ubuntu1.execute("sudo route del -net 10.0.1.0 netmask 255.255.255.0 gw 10.0.0.1")
        self.ubuntu1.execute("sudo ifconfig eth1 0.0.0.0")
        self.ubuntu1.disconnect()

        self.ubuntu2.execute("sudo ifconfig eth1 0.0.0.0")
        self.ubuntu2.disconnect()


