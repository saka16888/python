#!/usr/bin/env python

"""
Synopsis:
    Process config files (files that obey the .ini format):
    1. Print a report of several config files.
    2. Enable the user to enter section/name/value triples, then write
       a new config file.
    Sample config files are here -- config1.ini, config2.ini
Usage:
    python configfile_report_update.py [options] <file1> <file2> ...
Options:
    -o, --ouput     Output file name.  Default: tmp.ini
Hints:
    - ConfigParser module in the Python standard library
    - raw_input built-in function
"""

import sys
import getopt
import ConfigParser


def report(names):
    parser = ConfigParser.RawConfigParser()
    parser.read(names)
    sections = parser.sections()
    for section in sections:
        print 'section: %s' % (section, )
        items = parser.items(section)
        for name, value in items:
            print '    name: "%s"  value: "%s"' % (name, value, )
    return parser


def update(parser, outfilename):
    #parser = ConfigParser.RawConfigParser()
    while True:
        section = raw_input('Enter section: ')
        if not section:
            break
        name = raw_input('Enter option name: ')
        if not name:
            continue
        value = raw_input('Enter value: ')
        if not value:
            continue
        if not parser.has_section(section):
            parser.add_section(section)
        parser.set(section, name, value)
    outfile = open(outfilename, 'w')
    parser.write(outfile)
    outfile.close()


def test(names, outfilename):
    parser = report(names)
    answer = raw_input('update? y/[n]): ')
    if answer == 'y':
        update(parser, outfilename)


def main():
    args = sys.argv[1:]
    try:
        opts, args = getopt.getopt(args, 'o:', [
            '--output', ])
    except:
        sys.exit(__doc__)
    output = 'tmp.ini'
    for opt, val in opts:
        if opt in ('-o', '--output'):
            output = val
    if len(args) < 1:
        sys.exit(__doc__)
    test(args, output)


if __name__ == '__main__':
    main()
