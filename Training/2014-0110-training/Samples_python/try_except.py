#!/usr/bin/env python

import sys


def count_lines(filename):
    with open(filename, 'r') as infile:
        count = len(infile.readlines())
        return count


def process_file(filename):
    try:
        print '(process_file) before count_lines'
        count = count_lines(filename)
    finally:
        print '(process_file) after count_lines'
    return count


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        sys.stderr.write('usage: xxxx.py <file-name-pattern>\n')
        sys.exit(1)
    #count_lines(args[0])
    try:
        print 'line count: %d' % process_file(args[0])
    except IOError as exp:
        print 'file not found -- %s' % exp
    else:
        print 'everything is OK'
    finally:
        print 'doing some important cleanup'


if __name__ == '__main__':
    main()
