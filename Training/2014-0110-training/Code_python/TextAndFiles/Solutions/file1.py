#!/usr/bin/env python

"""
Read the lines in a file as a single string.

Print each line.
Count the "words" in the file.
Usage:
    python file1.py infilename
"""

import sys


def show_lines(infilename):
    infile = open(infilename)
    content = infile.read()
    infile.close()
    lines = content.splitlines()
    count = 0
    print '-' * 50
    for line in lines:
        print '* line:', line
        words = line.split()
        count += len(words)
    print '-' * 50
    print 'Number of words: %d' % count


def usage():
    print __doc__
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    show_lines(infilename)

if __name__ == '__main__':
    main()

