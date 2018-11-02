#!/usr/bin/env python

"""
Split a line into columns, then display the columns.

Usage:
    python columns.py [options] infilename
Options:
    -h, --help      Display this help message.
Example:
    python columns.py somefile.txt
"""


#
# Imports:
import sys
import getopt


def test(infilename):
    """Modify or replace this function for your own needs.
    """
    infile = open(infilename, 'r')
    for line in infile:
        fields = split_columns(line, (4, 5, 6, 3, 7, 6, 5))
        print '-' * 40
        for field in fields:
            print 'field: "%s"' % (field, )


def split_columns(line, spec):
    linelen = len(line)
    col1 = 0
    fields = []
    for col in spec:
        col2 = col1 + col
        if col2 > linelen:
            field = line[col1:-1]
            fields.append(field)
            break
        field = line[col1:col2]
        fields.append(field)
        col1 = col2
    return fields


USAGE_TEXT = __doc__


def usage():
    print USAGE_TEXT
    sys.exit(1)


def main():
    args = sys.argv[1:]
    try:
        opts, args = getopt.getopt(
            args, 'h', ['help', ])
    except:
        usage()
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
    if len(args) != 1:
        usage()
    infilename = args[0]
    test(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
