#!/usr/bin/env python

"""
Create a relational database and a table in it.
Add some records.
Read and display the records.
"""

import sys
import sqlite3


def create_table(db_name):
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE plants
    (name text, desc text, cat int)''')
    cursor.execute(
        "INSERT INTO plants VALUES ('tomato', 'red and juicy', 1)")
    cursor.execute(
        "INSERT INTO plants VALUES ('pepper', 'green and crunchy', 2)")
    cursor.execute(
        "INSERT INTO plants VALUES ('eggplant', 'purple', 2)")
    cursor.execute(
        "INSERT INTO plants VALUES "
        "('kabocha_squash', 'a tasty winter squash', 3)")
    con.commit()
    con.close()


def retrieve(db_name):
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    cursor.execute('''select * from plants''')
    rows = cursor.fetchall()
    print rows
    print '-' * 40
    cursor.execute('''select * from plants''')
    for row in cursor:
        print row
    con.close()


def main():
    args = sys.argv[1:]
    if len(args) == 0:
        db_name = 'data1.db'
    elif len(args) == 1:
        if args[0] == '-h' or args[0] == '--help':
            sys.stderr.write('\nusage: test_db.py <db_name>\n\n')
            sys.exit(-1)
        else:
            db_name = args[0]
    else:
        sys.stderr.write('\nusage: test_db.py <db_name>\n\n')
        sys.exit(1)
    create_table(db_name)
    retrieve(db_name)


if __name__ == '__main__':
    main()
