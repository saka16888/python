"""
unit_tests7a.py
"""

import unittest
import unit_tests_dbg


class UnitTests03(unittest.TestCase):

    def test_foo(self):
        unit_tests_dbg.dbgprint('testing test_foo (03)')
        self.assertTrue(True)

    def check_bar01(self):
        unit_tests_dbg.dbgprint('testing checkBar01')
        self.assertTrue(True)


class UnitTests04(unittest.TestCase):

##     def setUp(self):
##         print 'setting up UnitTests01'
##
##     def tearDown(self):
##         print 'tearing down UnitTests01'

    def test_bar01(self):
        unit_tests_dbg.dbgprint('testing test_bar01 (04)')
        self.assertTrue(True)

    def test_bar02(self):
        unit_tests_dbg.dbgprint('testing test_bar02 (04)')
        self.assertTrue(True)
