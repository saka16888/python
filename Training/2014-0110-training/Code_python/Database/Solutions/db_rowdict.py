#!/usr/bin/env python

"""
Sample code for creating a dictionary for a row with the Python DB API.
"""

import sys
import new
import sqlite3


def showdb():
    connection, cursor = opendb()
    showdb1(cursor)
    hr()
    showdb2(cursor)
    hr()
    showdb3(cursor)
##     hr()
##     showdb4(cursor)
##     connection.close()


def showdb1(cursor):
    print '*** showdb1 ***'
    cursor.execute("select * from plants order by name")
    hr()
    description = cursor.description
    print description
    print 'description:'
    for rowdescription in description:
        print '    %s' % (rowdescription, )
    hr()
    rows = cursor.fetchall()
    for row in rows:
        rowdict = make_row_dict(row, description)
        # print rowdict
        descrip = rowdict['desc']
        name = rowdict['name']
        rating = '%s' % rowdict['cat']
        print '    %s%s%s' % (
            name.ljust(12), descrip.ljust(30), rating.rjust(4), )


def showdb2(cursor):
    print '*** showdb2 ***'
    cursor.execute("select * from plants order by name")
    hr()
    description = cursor.description
    print description
    print 'description:'
    for rowdescription in description:
        print '    %s' % (rowdescription, )
    hr()
    rows = cursor.fetchall()
    for row in rows:
        rowdict = make_row_dict_obj1(row, description)
        # print rowdict
        descrip = rowdict['desc']
        name = rowdict['name']
        rating = '%s' % rowdict['cat']
        print '    %s%s%s' % (
            name.ljust(12), descrip.ljust(30), rating.rjust(4), )


def showdb3(cursor):
    print '*** showdb3 ***'
    cursor.execute("select * from plants order by name")
    hr()
    description = cursor.description
    print description
    print 'description:'
    for rowdescription in description:
        print '    %s' % (rowdescription, )
    hr()
    rows = cursor.fetchall()
    for row in rows:
        rowdict = make_row_dict_obj2(row, description)
        # print rowdict
        descrip = rowdict.desc
        name = rowdict.name
        rating = '%s' % rowdict.cat
        print '    %s%s%s' % (
            name.ljust(12), descrip.ljust(30), rating.rjust(4), )


def showdb4(cursor):
    print '*** showdb4 ***'
    cursor.execute("select * from plants order by name")
    hr()
    description = cursor.description
    print description
    print 'description:'
    for rowdescription in description:
        print '    %s' % (rowdescription, )
    hr()
    rows = cursor.fetchall()
    for row in rows:
        rowdict = make_row_dict_obj3(row, description)
        # print rowdict
        descrip = rowdict.desc
        name = rowdict.name
        rating = '%s' % rowdict.cat
        print '    %s%s%s' % (
            name, descrip, rating, )


def opendb():
    connection = sqlite3.connect("db_test01.db")
    cursor = connection.cursor()
    return connection, cursor


def make_row_dict(row, row_descriptions):
    rowdict = {}
    for idx, row_description in enumerate(row_descriptions):
        name = row_description[0].lower()
        rowdict[name] = row[idx]
    return rowdict


def make_row_dict_obj1(row, row_description):
    rowdict = RowDictionary1(row, row_description)
    return rowdict


def make_row_dict_obj2(row, row_description):
    rowdict = RowDictionary2(row, row_description)
    return rowdict


def make_row_dict_obj3(row, row_description):
    rowdict = RowDictionary3(row, row_description)
    return rowdict


class RowDictionary1(object):
    def __init__(self, row, row_descriptions):
        self.rowdict = {}
        for idx, row_description in enumerate(row_descriptions):
            name = row_description[0].lower()
            self.rowdict[name] = row[idx]
    def __getitem__(self, name):
        return self.rowdict[name]
    def __str__(self):
        return '<rowdictionary %s>' % (self.rowdict, )


class RowDictionary2(object):
    def __init__(self, row, row_descriptions):
        # Create the dictionary and insert an entry for each column.
        self.rowdict = {}
        for idx, row_description in enumerate(row_descriptions):
            name = row_description[0].lower()
            self.rowdict[name] = row[idx]
        # Create properties for each item in the dictionary.
        for name, val in self.rowdict.items():
            self.__dict__[name] = val
##     def __getitem__(self, name):
##         return self.rowdict[name]
    def __str__(self):
        return '<rowdictionary %s>' % (self.rowdict, )


class RowDictionary3(object):
    def __init__(self, row, row_descriptions):
        # Create the dictionary and insert an entry for each column.
        self.rowdict = {}
        for idx, row_description in enumerate(row_descriptions):
            name = row_description[0].lower()
            self.rowdict[name] = row[idx]
        # Create properties for each item in the dictionary.
        for name in self.rowdict:
            f = self.make_func(name)
            m = new.instancemethod(f, self, RowDictionary3)
            print dir(RowDictionary3.__dict__)
            RowDictionary3.__dict__[name] = property(m)
    def make_func(self, name):
        def inner(self):
            return self.rowdict[name]
        return inner
    def __getitem__(self, name):
        return self.rowdict[name]
    def __str__(self):
        return '<rowdictionary %s>' % (self.rowdict, )


def hr():
    print '-' * 60


def usage():
    print __doc__
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) < 0:
        usage()
    showdb()

if __name__ == '__main__':
    main()

