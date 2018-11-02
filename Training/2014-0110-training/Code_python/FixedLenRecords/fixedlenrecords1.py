#!/usr/bin/env python

"""
Write and read fixed length records.

Usage:
    python fixedlenrecords1.py filename
"""

import sys


def create_file(filename, length):
    outfile = open(filename, 'w')
    for item in 'abcdefghijklm':
        outfile.write(item * length)
    outfile.close()


def read_file(filename, length):
    infile = open(filename, 'r')
    data = infile.read(length)
    while data:
        print 'reading: "%s"' % data
        data = infile.read(length)
    infile.close()


def iter_records(infile, length):
    data = infile.read(length)
    while data:
        yield data
        data = infile.read(length)


def filter_records(records, predicate=None):
    for record in records:
        if predicate is None:
            yield record
        elif predicate(record):
            yield record


def predicate1(record):
    if (record.startswith('bbb') or
            record.startswith('ddd') or
            record.startswith('fff')):
        return False
    else:
        return True


def predicate2(record):
    if record[:3] > 'fff':
        return True
    else:
        return False


def hr():
    print '-' * 60


def usage():
    print __doc__
    sys.exit(1)


def test():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    filename = args[0]
    length = 20
    create_file(filename, length)
    # ---------------------------------------------------
    read_file(filename, length)
    # ---------------------------------------------------
    hr()
    infile = open(filename, 'r')
    for record in iter_records(infile, length):
        print 'iterating: "%s"' % record
    infile.close()
    # ---------------------------------------------------
    hr()
    infile = open(filename, 'r')
    for record in iter_records(infile, length):
        if predicate1(record):
            print 'filtered 1: "%s"' % record
    infile.close()
    # ---------------------------------------------------
    hr()
    infile = open(filename, 'r')
    records = iter_records(infile, length)
    for record in filter_records(records, predicate1):
        print 'filtered 2: "%s"' % record
    infile.close()
    # ---------------------------------------------------
    hr()
    infile = open(filename, 'r')
    for record in filter_records(iter_records(infile, length), predicate1):
        print 'filtered 3: "%s"' % record
    infile.close()
    # ---------------------------------------------------
    hr()
    infile = open(filename, 'r')
    for count, record in enumerate(
            filter_records(iter_records(infile, length), predicate2)):
        print 'filtered 4: %d. "%s"' % (count + 1, record, )
    infile.close()

if __name__ == '__main__':
    test()
