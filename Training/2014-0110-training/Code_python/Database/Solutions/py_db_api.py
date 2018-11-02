#!/usr/bin/env python

"""
Perform operations on sqlite3 (plants) database.
    connection.startup("dbtest1", "plantsdbdir")

Usage:
    python py_db_api.py <dbname> <command> [arg1, ... ]
Commands:
    create -- create new database.
    show -- show contents of database.
    add -- add row to database.  Requires 3 args (name, descrip, rating).
    delete - remove row from database.  Requires 1 arg (name).
Examples:
    python test1.py <dbname> create
    python test1.py <dbname> show
    python test1.py <dbname> add crenshaw "The most succulent melon" 10
    python test1.py <dbname> delete lemon
"""


import sys
import sqlite3

Values = [
    ('lemon', 'bright and yellow', '7'),
    ('peach', 'succulent', '9'),
    ('banana', 'smooth and creamy', '8'),
    ('nectarine', 'tangy and tasty', '9'),
    ('orange', 'sweet and tangy', '8'),
]

Field_defs = [
    'p_name varchar',
    'p_descrip varchar',
    #'p_rating integer',
    'p_rating varchar',
]


def createdb(dbname):
    connection = sqlite3.connect(dbname)
    cursor = connection.cursor()
    q1 = "create table plants (%s)" % (', '.join(Field_defs))
    print 'create q1: %s' % q1
    cursor.execute(q1)
    q1 = "create index index1 on plants(p_name)"
    cursor.execute(q1)
    q1 = (
        "insert into plants (p_name, p_descrip, p_rating) values " +
        "('%s', '%s', %s)"
    )
    for spec in Values:
        q2 = q1 % spec
        print 'q2: "%s"' % q2
        cursor.execute(q2)
    connection.commit()
    showdb1(cursor)
    connection.close()


def showdb(dbname):
    connection, cursor = opendb(dbname)
    showdb1(cursor)
    connection.close()


def showdb1(cursor):
    cursor.execute("select * from plants order by p_name")
    hr()
    description = cursor.description
    print description
    print 'description:'
    for rowdescription in description:
        print '    %s' % (rowdescription, )
    hr()
    rows = cursor.fetchall()
    print rows
    print 'rows:'
    for row in rows:
        print '    %s' % (row, )
    hr()
    print 'content:'
    for row in rows:
        descrip = row[1]
        name = row[2]
        rating = '%s' % row[0]
        print '    %s%s%s' % (
            name.ljust(12), descrip.ljust(30), rating.rjust(4), )


def addtodb(dbname, name, descrip, rating):
    try:
        rating = int(rating)
    except ValueError:
        print 'Error: rating must be integer.'
        return
    connection, cursor = opendb(dbname)
    cursor.execute("select * from plants where p_name = '%s'" % name)
    rows = cursor.fetchall()
    if len(rows) > 0:
        ql = (
            "update plants set p_descrip='%s', p_rating='%s' "
            "where p_name='%s'"
        ) % (
            descrip, rating, name, )
        print 'ql:', ql
        cursor.execute(ql)
        connection.commit()
        print 'Updated'
    else:
        cursor.execute("insert into plants values ('%s', '%s', '%s')" % (
            name, descrip, rating))
        connection.commit()
        print 'Added'
    showdb1(cursor)
    connection.close()


def deletefromdb(dbname, name):
    connection, cursor = opendb(dbname)
    cursor.execute("select * from plants where p_name = '%s'" % name)
    rows = cursor.fetchall()
    if len(rows) > 0:
        cursor.execute("delete from plants where p_name='%s'" % name)
        connection.commit()
        print 'Plant (%s) deleted.' % name
    else:
        print 'Plant (%s) does not exist.' % name
    showdb1(cursor)
    connection.close()


def opendb(dbname):
    connection = sqlite3.connect(dbname)
    cursor = connection.cursor()
    return connection, cursor


def hr():
    print '-' * 60


def usage():
    print __doc__
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) < 2:
        usage()
    dbname = args[0]
    cmd = args[1]
    if cmd == 'create':
        if len(args) != 2:
            usage()
        createdb(dbname)
    elif cmd == 'show':
        if len(args) != 2:
            usage()
        showdb(dbname)
    elif cmd == 'add':
        if len(args) < 5:
            usage()
        name = args[2]
        descrip = args[3]
        rating = args[4]
        addtodb(dbname, name, descrip, rating)
    elif cmd == 'delete':
        if len(args) < 3:
            usage()
        name = args[2]
        deletefromdb(dbname, name)
    else:
        usage()

if __name__ == '__main__':
    main()
