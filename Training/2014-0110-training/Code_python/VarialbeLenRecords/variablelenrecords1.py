#!/usr/bin/env python

"""
Write and read variable length records.

The record length (the length of the data payload) is stored in the
first two characters of the record.

Usage:
    python variablelenrecords1.py filename
"""

import sys

def create_file(filename):
    outfile = open(filename, 'w')
    for letter in 'abcdefghijklm':
        write_one_record(outfile, letter)
    outfile.close()

def write_one_record(outfile, letter):
    length = ord(letter) - 90
    record = '%02d%s' % (length, letter * length, )
    outfile.write(record)

def read_file(filename):
    infile = open(filename, 'r')
    data = read_one_record(infile)
    while data:
        print 'reading: "%s"' % data
        data = read_one_record(infile)
    infile.close()

def read_one_record(infile):
    chrlength = infile.read(2)
    if len(chrlength) < 2:
        return ''
    length = int(chrlength)
    record = infile.read(length)
    return record

def iter_records(infile):
    data = read_one_record(infile)
    while data:
        yield data
        data = read_one_record(infile)

def filter_records(records, predicate=None):
    for record in records:
        if predicate is None:
            yield record
        elif predicate(record):
            yield record

def predicate1(record):
    if (record.startswith('bbb') or
        record.startswith('ddd') or
        record.startswith('fff')
        ):
        return False
    else:
        return True

def predicate2(record):
    if ord(record[0]) % 2 == 0:
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
    create_file(filename)
    # ---------------------------------------------------
    read_file(filename)
    # ---------------------------------------------------
    hr()
    infile = open(filename, 'r')
    for record in iter_records(infile):
        print 'iterating: "%s"' % record
    infile.close()
    # ---------------------------------------------------
    hr()
    infile = open(filename, 'r')
    for record in iter_records(infile):
        if predicate1(record):
            print 'filtered 1: "%s"' % record
    infile.close()
    # ---------------------------------------------------
    hr()
    infile = open(filename, 'r')
    records = iter_records(infile)
    for record in filter_records(records, predicate1):
        print 'filtered 2: "%s"' % record
    infile.close()
    # ---------------------------------------------------
    hr()
    infile = open(filename, 'r')
    for record in filter_records(iter_records(infile), predicate1):
        print 'filtered 3: "%s"' % record
    infile.close()
    # ---------------------------------------------------
    hr()
    infile = open(filename, 'r')
    for count, record in enumerate(filter_records(iter_records(infile),
        predicate2)):
        print 'filtered 4: %d. "%s"' % (count + 1, record, )
    infile.close()

if __name__ == '__main__':
    test()
