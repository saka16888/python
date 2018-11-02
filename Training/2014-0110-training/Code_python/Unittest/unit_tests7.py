#!/usr/bin/env python

"""
unit_tests7.py

Sample unittest -- Loading unit tests from multiple modules.
"""

import unittest
import unit_tests7a
import unit_tests7b
import unit_tests_dbg


class UnitTests02(unittest.TestCase):

    def test_foo(self):
        unit_tests_dbg.dbgprint('testing test_foo (02)')
        self.assertTrue(True)

    def check_bar01(self):
        unit_tests_dbg.dbgprint('testing checkBar01 (02)')
        self.assertTrue(True)


class UnitTests01(unittest.TestCase):

##     def setUp(self):
##         print 'setting up UnitTests01'

##     def tearDown(self):
##         print 'tearing down UnitTests01'

    def test_bar01(self):
        unit_tests_dbg.dbgprint('testing test_bar01 (01)')
        self.assertTrue(True)

    def test_bar02(self):
        unit_tests_dbg.dbgprint('testing test_bar02 (01)')
        self.assertTrue(True)


def function_test_1():
    unit_tests_dbg.dbgprint('testing function_test_1')
    assert(True)


def function_test_1_setup():
    print 'setup for function_test_1'


def function_test_1_teardown():
    print 'teardown for function_test_1'


def make_suite():
    suite = unittest.TestSuite()
    loader = unittest.defaultTestLoader
    suite.addTest(unittest.makeSuite(UnitTests01))
    suite.addTest(unittest.makeSuite(UnitTests02))
    suite.addTest(loader.loadTestsFromModule(unit_tests7a))
    suite.addTest(loader.loadTestsFromModule(unit_tests7b))
    suite.addTest(unittest.FunctionTestCase(
        function_test_1,
        setUp=function_test_1_setup,
        tearDown=function_test_1_teardown))
    return suite


def main():
    suite = make_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    main()
