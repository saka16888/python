#!/usr/bin/env python

"""
unit_tests3.py

Sample unittest -- Simple main() runner with prefix and sort.
"""


import unittest
import unit_tests_dbg


class UnitTests02(unittest.TestCase):

    def test_foo(self):
        unit_tests_dbg.dbgprint('test_foo')
        self.assertTrue(True)


class UnitTests01(unittest.TestCase):

    def test_bar01(self):
        unit_tests_dbg.dbgprint('testBar01')
        self.assertTrue(True)

    def test_bar02(self):
        unit_tests_dbg.dbgprint('testBar02')
        self.assertTrue(True)

    def check_bar01(self):
        unit_tests_dbg.dbgprint('checkBar01')
        self.assertTrue(True)

    def check_bar02(self):
        unit_tests_dbg.dbgprint('checkBar02')
        self.assertTrue(True)


def my_cmp(a, b):
    if a > b:
        return -1
    elif a < b:
        return 1
    else:
        return 0


def main():
    unit_tests_dbg.dbgprint(unittest.getTestCaseNames(UnitTests01, 'test'))
    loader = unittest.defaultTestLoader
    loader.testMethodPrefix = 'check'
    loader.sortTestMethodsUsing = my_cmp
    unittest.main(testLoader=loader)

if __name__ == '__main__':
    main()
