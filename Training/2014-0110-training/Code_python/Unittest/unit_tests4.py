#!/usr/bin/env python

"""
unit_tests4.py

Sample unittest -- Unit test suite with prefix and sort plus tests from
    multiple unit test classes.
"""

import unittest
import unit_tests_dbg


class UnitTests02(unittest.TestCase):

    def test_foo(self):
        unit_tests_dbg.dbgprint('testing test_foo')
        self.assertTrue(True)

    def check_bar01(self):
        unit_tests_dbg.dbgprint('testing checkBar01')
        self.assertTrue(True)


class UnitTests01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        unit_tests_dbg.dbgprint('class set up UnitTests01')

    @classmethod
    def tearDownClass(cls):
        unit_tests_dbg.dbgprint('class tear down UnitTests01')

    def setUp(self):
        unit_tests_dbg.dbgprint('setting up UnitTests01')

    def tearDown(self):
        unit_tests_dbg.dbgprint('tearing down UnitTests01')

    def test_bar01(self):
        unit_tests_dbg.dbgprint('testing test_bar01')
        self.assertTrue(True)

    def test_bar02(self):
        unit_tests_dbg.dbgprint('testing test_bar02')
        self.assertTrue(True)


def function_test_1():
    name = 'albert'
    assert name.startswith('al')


def compare_names(name1, name2):
    """ Sort in reverse alphabetic order.
    """
    if name1 < name2:
        return 1
    elif name1 > name2:
        return -1
    else:
        return 0


def make_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(UnitTests01, sortUsing=compare_names))
    suite.addTest(unittest.makeSuite(UnitTests02, prefix='check'))
    suite.addTest(unittest.FunctionTestCase(function_test_1))
    return suite


def main():
    suite = make_suite()
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)

if __name__ == '__main__':
    main()
