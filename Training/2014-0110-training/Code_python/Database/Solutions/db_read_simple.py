#!/usr/bin/env python

"""
Sample of simple database query using the Python DB API.

Show how to use the cursor object (1) to fetch rows and
(2) to use the cursor object as an iterable.
"""

import sys
import sqlite3


def test():
    args = sys.argv[1:]
    if len(args) != 1:
        sys.stderr.write('\nusage: python db_read_simple.py <dbname>\n')
        sys.exit(1)
    dbname = args[0]
    connection = sqlite3.connect(dbname)
    cursor = connection.cursor()
    hr('Show rows using cursor as an iterable.')
    cursor.execute('select * from plants order by name')
    for row in cursor:
        print '1. row:', row
    hr('Show rows using fetchall().')
    cursor.execute('select * from plants order by name')
    rows = cursor.fetchall()
    for row in rows:
        print '2. row:', row
    hr('Show field descriptions')
    cursor.execute('select * from plants order by name')
    for field in cursor.description:
        print 'field:', field
    for row in cursor:
        for idx, field in enumerate(row):
            content = '%s: "%s"' % (cursor.description[idx][0], field, )
            print content,
        print
    connection.close()


def hr(msg):
    print '-' * 50
    print msg
    print '-' * 50


if __name__ == '__main__':
    test()
