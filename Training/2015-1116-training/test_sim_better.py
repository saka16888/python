# Goals:  Make tests reusable with parameters and functions
#         Group related tests in classes
#         Add documentation
#         Show how the aetest.main() function works.
#         Improve logging

import topology
import aetest
import parsers

def dialin():
    tb = topology.load('sim_test.yaml')
    dev = tb.devices['pyats-asa-1']
    dev.connect()
    dev.config('''
        interface GigabitEthernet0/0
          nameif inside
          security-level 100
          ip address 10.0.0.1 255.255.255.0
          no shut
    ''')
    return dev

def restore(dev):
    dev.config('''
        clear config object
        clear config access-group
        clear config interface g0/0
    ''')
    dev.disconnect()

class PingTests(aetest.Testcase):
    'Verify connection quality using ``ping``'

    def test_no_ping_packets_lost(self):
        'Verify that a ping had 0% packet loss'
        dev = dialin()
        output = dev.execute('ping www.cisco.com')
        ping_result = parsers.parse_ping(output)
        assert ping_result.loss_rate == 0.0
        restore(dev)

    verify_not_too_many_ipv4_up_interfaces_unassigned.test = True

class IPV4_Interface_Tests(aetest.Testcase):
    "Verify IPV4 interfaces don't violate basic macaddress and irq constraints"

    def verify_minimum_ipv4_interfaces_up(self):
        'Verify that at least 5 ipv4 interfaces are "Up"'
        dev = dialin()
        output = dev.execute('show ipv4 int bri')
        interfaces = parsers.parse_interfaces(output)
        assert sum([interface.status=='up' for interface in interfaces]) > 5
        restore(dev)

    verify_minimum_ipv4_interfaces_up.test = True

    def verify_not_too_many_ipv4_up_interfaces_unassigned(self):
        'Verify that no more that 6 of the ipv4 up interfaces are "unassigned"'
        dev = dialin()
        output = dev.execute('show ipv4 int bri')
        interfaces = parsers.parse_interfaces(output)
        assert sum([interface.ipaddr == 'unassigned' for interface in interfaces if interface.status=='up']) <= 6
        restore(dev)

    verify_not_too_many_ipv4_up_interfaces_unassigned.test = True
if  __name__ == '__main__':
    testcases = [PingTests(), IPV4_Interface_Tests()] 
    aetest.run_tests(testcases)

