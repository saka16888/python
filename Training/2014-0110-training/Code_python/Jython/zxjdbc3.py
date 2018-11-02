#!/usr/bin/env python

"""
Sample use of zxJDBC to read and update PostgreSQL database.

Usage -- Use "-h" to see options and commands.

Requirement -- add the JDBC driver to your CLASSPATH.  For example,
in my case I added:

    postgresql-8.2-506.jdbc4.jar

"""

import sys
import getopt
from com.ziclix.python.sql import zxJDBC


CONNECT_ARGS = (
    "jdbc:postgresql://thrush:5432/test",
    "postgres",
    "Flicker",
    "org.postgresql.Driver",
)


def showPlants(args):
    if len(args) != 0:
        usage()
    con = zxJDBC.connect(*CONNECT_ARGS)
    cur = con.cursor()
    while 1:
        showPlants1(cur)
        response = raw_input('Press Enter to continue; "q" to quit: ')
        if response.lower() == 'q':
            break
    cur.close()
    con.close()


def showPlants1(cur):
    cur.execute("select * from Plant_DB order by p_name")
    print '=' * 60
    rows = cur.fetchall()
    print 'id(rows): %x' % id(rows)
    print '\nName:               Description:            Rating:'
    print '=====               ============            ======'
    for row in rows:
        print '%s%s%s' % (row[0].ljust(20), row[1].ljust(24), row[2])
    print ''


def showPlantsDescription(args):
    if len(args) != 0:
        usage()
    con = zxJDBC.connect(*CONNECT_ARGS)
    cur = con.cursor()
    cur.execute("select * from Plant_DB order by p_name")
    print '\nName:               Type:               Rating:'
    print '=====               =====               ====='
    for item in cur.description:
        print '%s%s%s' % (
            str(item[0]).ljust(20),
            str(item[1]).ljust(20),
            str(item[2]))
    print
    cur.close()
    con.close()


def addPlant(args):
    if len(args) != 3:
        usage()
    name = args[0]
    descrip = args[1]
    rating = args[2]
    con = zxJDBC.connect(*CONNECT_ARGS)
    cur = con.cursor()
    cur.execute("select * from Plant_DB where p_name = '%s'" % name)
    row = cur.fetchone()
    if row:
    #if cur.rowcount == 1:
        sql = "update Plant_DB set p_desc='%s', p_rating='%s' where p_name='%s'" % \
            (descrip, rating, name)
        print 'sql:', sql
        cur.execute(sql)
        con.commit()
        print 'Updated'
    else:
        cur.execute("insert into Plant_DB values ('%s', '%s', '%s')" % (
            name, descrip, rating))
        con.commit()
        print 'Added'
    showPlants1(cur)
    cur.close()
    con.close()


def deletePlant(args):
    if len(args) != 1:
        usage()
    name = args[0]
    con = zxJDBC.connect(*CONNECT_ARGS)
    cur = con.cursor()
    query = "select * from Plant_DB where p_name = '%s'" % name
    cur.execute(query)
    row = cur.fetchone()
    if row:
    #if cur.rowcount > 0:
        cur.execute("delete from Plant_DB where p_name='%s'" % name)
        con.commit()
        print 'Plant (%s) deleted.' % name
    else:
        print 'Plant (%s) does not exist.' % name
    showPlants1(cur)
    cur.close()
    con.close()


def save(con, fileName):
    pass


def load(fileName):
    connection = None
    return connection


def saveConnection(args):
    if len(args) != 1:
        usage()
    fileName = args[0]
    con = zxJDBC.connect(*CONNECT_ARGS)
    cur = con.cursor()
    cur.execute("select * from Plant_DB order by p_name")
    save(con, fileName)


def loadConnection(args):
    if len(args) != 1:
        usage()
    fileName = args[0]
    connection = load(fileName)
    cursor = connection.cursor()
    cursor.execute("select * from Plant_DB")
    rows = cursor.fetchall()
    print 'rows:', rows


def showHelp(args):
    usage()


USAGE_TEXT = """
Usage: python plantstable.py --option [ args ]
Options:
"""

OPTIONS = (
    ('showplants', showPlants,
        'Show the plants table'),
    ('addplant', addPlant,
        'Add/update the plants table. Args: <name> <descript> <rating>'),
    ('showdescription', showPlantsDescription,
        'Show the description of columns in the plants tabele'),
    ('saveconnection', saveConnection,
        'Create and save a connection'),
    ('loadconnection', loadConnection,
        'Load and re-use a connection'),
     ('deleteplant', deletePlant,
        'Delete an existing plant. Args: <name>'),
     ('help', showHelp,
        'Show this help message')
)

def usage():
    print USAGE_TEXT
    for option in OPTIONS:
        print '  --%s -- %s' % (option[0].ljust(16), option[2])
    sys.exit(-1)


def main():
    args = sys.argv[1:]
    optionNames = []
    for option in OPTIONS:
        optionNames.append(option[0])
    options, args = getopt.getopt(args, '', optionNames)
    if len(options) != 1:
        usage()
    optionName = options[0][0]
    found = 0
    for option in OPTIONS:
        if optionName[2:] == option[0]:
            option[1](args)
            found = 1
            break
    if not found:
        usage()


if __name__ == '__main__':
    main()
    #import pdb
    #pdb.run('main()')
