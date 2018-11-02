#!/usr/bin/env python

"""
unit_tests1.py

Sample unittest -- Simple main() runner.
"""

import unittest
import unit_tests_dbg


class UnitTests02(unittest.TestCase):

    def test_foo(self):
        unit_tests_dbg.dbgprint('test #1')
        self.assertTrue(True)


class UnitTests01(unittest.TestCase):

    def test_bar01(self):
        unit_tests_dbg.dbgprint('test #2')
        self.assertTrue(True)

    def test_bar02(self):
        unit_tests_dbg.dbgprint('test #3')
        self.assertFalse(False)


def main():
    unit_tests_dbg.dbgprint(unittest.getTestCaseNames(UnitTests01, 'test'))
    unittest.main()

if __name__ == '__main__':
    main()
