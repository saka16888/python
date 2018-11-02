#!/usr/bin/env python

"""
Micro library for access to a sqlite3 database.

Create the database with db_create_simple.py.

>>> import unit_tests_lib
>>> import sqlite3
>>> connection = sqlite3.connect('data1.db')
>>> unit_tests_lib.fetch_rows(connection)
[(u'eggplant', u'purple', 2), (u'kabocha_squash', u'a tasty winter squash', 3), (u'pepper', u'green and crunchy', 2), (u'tomato', u'red and juicy', 1)]
>>> unit_tests_lib.fetch_column(connection, 'name')
[(u'eggplant',), (u'kabocha_squash',), (u'pepper',), (u'tomato',)]

"""

import sys
import sqlite3


def fetch_rows(connection):
    """Fetch and return all the rows from the database.
    """
    cursor = connection.cursor()
    cursor.execute('select * from plants order by name')
    rows = cursor.fetchall()
    return rows


def fetch_column(connection, column_name):
    """Fetch the values from a specific column in the database.
    Possible columns are 'name', 'desc', 'cat'.
    """
    cursor = connection.cursor()
    query = 'select %s from plants order by name' % column_name
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows


def test():
    args = sys.argv[1:]
    if len(args) != 1:
        sys.stderr.write('\nusage: python unit_tests_lib.py <db_name>\n')
        sys.exit(1)
    db_name = args[0]
    connection = sqlite3.connect(db_name)
    rows = fetch_rows(connection)
    print 'rows:'
    for row in rows:
        print '    %s' % (row, )
    column_values = fetch_column(connection, 'name')
    print 'column values:'
    for value in column_values:
        print '    "%s"' % value
    connection.close()


if __name__ == '__main__':
    test()
    #import doctest
    #doctest.testmod()
