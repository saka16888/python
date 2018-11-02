

from ats import topology
from ats import aetest
import logging

LOGGER = logging.getLogger(__name__)

class VersionTestSuite(aetest.Testcase):

    @aetest.setup
    def dialin(self):
        testbed_file = self.parameters['testbed_file']
        tb = topology.loader.load(testbed_file)
        asa = tb.devices['pyats-asa-1']
        asa.connect(alias='vty1', via='vty1')
        self.parameters['asa'] = asa

    @aetest.test
    def verify_enforce(self):
        'Verify licensing enforce mode is either evaluation or authorized'
        asa = self.parameters['asa']
        output = asa.vty1.execute('show version')
        LOGGER.info('Successfully retrieved version:\n%s' % output)
        assert 'enforce mode: Authorized' in output or 'enforce mode: Eval' in output, \
               'Expected the Licensing enforce mode to be Eval or Authorized'

    @aetest.test
    def verify_failover(self):
        'Check for Active/Active or Active/Standby failover'
        asa = self.parameters['asa']
        output = asa.vty1.execute('show version')
        LOGGER.info('Successfully retrieved version:\n%s' % output)
        assert 'Active/Standby' in output or 'Active/Active' in output, \
               'Check failover in the licensed features'

    @aetest.cleanup
    def windup(self):
        asa = self.parameters['asa']
        asa.vty1.disconnect()

if __name__ == '__main__':
    aetest.main(testbed_file='../etc/pyclass.yaml')





