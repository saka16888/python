#!/usr/bin/env python

"""Print out a report of the data in a CSV (comma separated values).

Usage:
    python csv_report.py infilename
"""

#
# Imports:
import sys
import csv


def proc_file1(infilename):
    """
    """
    infile = open(infilename, 'r')
    print 'Name        Description              Rating'
    print '====        ===========              ======'
    for line in infile:
        proc_line1(line)
    infile.close()


def proc_line1(line):
    if line[0] != '#':
        line = line.rstrip()
        fields = line.split(',')
        if len(fields) != 3:
            print 'strange line: %s' % (line, )
        else:
            name = fields[0]
            desc = fields[1]
            rating = fields[2]
            print '%s%s%s' % (
                name.ljust(12), desc.ljust(24), rating.rjust(7), )


def proc_file2(infilename):
    with open(infilename, 'r') as infile:
        reader = csv.reader(infile)
        print 'Name        Description              Rating'
        print '====        ===========              ======'
        for line in reader:
            proc_line2(line)


def proc_line2(fields):
    if not fields[0].startswith('#'):
        if len(fields) != 3:
            print 'strange line: %s' % (fields, )
        else:
            name = fields[0]
            desc = fields[1]
            rating = fields[2]
            print '%s%s%s' % (
                name.ljust(12), desc.ljust(24), rating.rjust(7), )


def usage():
    print __doc__
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    print '\n---------- Processing with line.split() ----------\n'
    proc_file1(infilename)
    print '\n---------- Processing with csv module   ----------\n'
    proc_file2(infilename)
    print


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
