'Show, in minature, what the real aetest package is all about'

import logging

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class Testcase:
    pass

def run_tests(testcase):
    for attr in dir(testcase):
        test = getattr(testcase, attr)
        LOGGER.info('Running teststep: %r', test.__name__)
        try:
            test()
        except AssertionError:
            LOGGER.exception('Failed teststep: %r', test.__name__)
        else:
            LOGGER.info('Successful teststep: %r', test.__name__)

