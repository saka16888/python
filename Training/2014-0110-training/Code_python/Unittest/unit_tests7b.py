"""
unit_tests7b.py
"""

import unittest
import unit_tests_dbg


class UnitTests05(unittest.TestCase):

##     def setUp(self):
##         print 'setting up UnitTests01'
##
##     def tearDown(self):
##         print 'tearing down UnitTests01'

    def test_bar01(self):
        unit_tests_dbg.dbgprint('testing test_bar01 (05)')
        self.assertTrue(True)

    def test_bar02(self):
        unit_tests_dbg.dbgprint('testing test_bar02 (05)')
        self.assertTrue(True)
