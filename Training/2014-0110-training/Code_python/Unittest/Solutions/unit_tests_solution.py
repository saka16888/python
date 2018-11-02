#!/usr/bin/env python

"""
Unit tests for the unit_tests_lib module using sqlite3.
"""

import unittest
import sqlite3
import unit_tests_lib
import unit_tests_dbg


class TestDB1(unittest.TestCase):
    """Tests for the database access functions in unit_test_lib.
    """

    db_name = 'data1.db'

    def test_01_fetch_rows(self):
        connection = sqlite3.connect(self.db_name)
        rows = unit_tests_lib.fetch_rows(connection)
        self.assertEqual(len(rows), 4)
        connection.close()

    def test_02_fetch_column(self):
        connection = sqlite3.connect(self.db_name)
        values = unit_tests_lib.fetch_column(connection, 'name')
        self.assertEqual(len(values), 4)
        connection.close()


class TestDB2(unittest.TestCase):
    """Tests for the database access functions in unit_test_lib.

    Factor out initialization and cleanup into the setUp and tearDown
    methods.
    """

    db_name = 'data1.db'

    def setUp(self):
        unit_tests_dbg.dbgprint('TestDB2.setUp')
        self.connection = sqlite3.connect(self.db_name)

    def tearDown(self):
        unit_tests_dbg.dbgprint('TestDB2.tearDown')
        self.connection.close()

    def test_01_fetch_rows(self):
        rows = unit_tests_lib.fetch_rows(self.connection)
        self.assertEqual(len(rows), 4)

    def test_02_fetch_column(self):
        values = unit_tests_lib.fetch_column(self.connection, 'name')
        self.assertEqual(len(values), 4)


class TestDB3(unittest.TestCase):
    """Tests for the database access functions in unit_test_lib.

    Factor out initialization and cleanup into the setUp and tearDown
    *class* methods.
    """

    db_name = 'data1.db'

    @classmethod
    def setUpClass(cls):
        unit_tests_dbg.dbgprint('TestDB3.setUpClass')
        cls.connection = sqlite3.connect(cls.db_name)

    @classmethod
    def tearDownClass(cls):
        unit_tests_dbg.dbgprint('TestDB3.tearDownClass')
        cls.connection.close()

    def test_01_fetch_rows(self):
        rows = unit_tests_lib.fetch_rows(self.connection)
        self.assertEqual(len(rows), 4)

    def test_02_fetch_column(self):
        values = unit_tests_lib.fetch_column(self.connection, 'name')
        self.assertEqual(len(values), 4)


def get_suite():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestDB3)
    return suite


def main():
    suite = get_suite()
    # verbosity = 0 (none) or 1 (dots) or 2 (name/description)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    main()
