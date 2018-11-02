#!/usr/bin/env python

"""
Sample use of zxJDBC to read PostgreSQL database.

Requirement -- add the JDBC driver to your CLASSPATH.  For example,
in my case I added:

    postgresql-8.2-506.jdbc4.jar

"""

import sys
import getopt
from com.ziclix.python.sql import zxJDBC


def test():
    d, u, p, v = (
        "jdbc:postgresql://thrush:5432/test",
        "postgres",
        "Flicker",
        "org.postgresql.Driver",
        )
    print '1. starting'
    db = zxJDBC.connect(d, u, p, v)
    print '2. connected'
    cur = db.cursor()
    print dir(cur)
    print '3. got cursor'
    for idx in range(10):
        print '=' * 30
        print 'Iteration %d' % (idx + 1, )
        cur.execute('select * from plant_db')
        print '4. executed'
        rows = cur.fetchall()
        print '5. fetched'
        s1 = '%s %s %s' % (
            'Name'.ljust(12),
            'Description'.ljust(24),
            'Rating'.ljust(10),
            )
        print s1
        s1 = '%s %s %s' % (
            '===='.ljust(12),
            '==========='.ljust(24),
            '======'.ljust(10),
            )
        print s1
        for row in rows:
            rating = str(row[2])
            print '%s %s %s' % (
                row[0].ljust(12), row[1].ljust(24), rating.ljust(10), )
    cur.close()
    db.close()


USAGE_TEXT = """
Usage:
    python test_jdbc.py [options]
Options:
    -h, --help      Display this help message.
Example:
    python test_jdbc.py
"""

def usage():
    print USAGE_TEXT
    sys.exit(-1)


def main():
    args = sys.argv[1:]
    try:
        opts, args = getopt.getopt(args, 'h', ['help',])
    except:
        usage()
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
    if len(args) != 0:
        usage()
    for idx in range(5):
        print '*' * 50
        test()


if __name__ == '__main__':
    main()
    #import pdb
    #pdb.run('main()')
