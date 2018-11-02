#!/usr/bin/env python
"""
Print a report of a config file and construct and pretty print a dictionary.
"""

import sys
import os
from ConfigParser import ConfigParser
import pprint


def print_report(parser):
    sections = parser.sections()
    for section in sections:
        options = parser.options(section)
        for option in options:
            value = parser.get(section, option)
            print '%s:%s: %s' % (section, option, value, )


def construct_table(parser):
    table = {}
    sections = parser.sections()
    for section in sections:
        subtable = {}
        table[section] = subtable
        options = parser.options(section)
        for option in options:
            value = parser.get(section, option)
            subtable[option] = value
    return table


def add_items(parser):
    sections = parser.sections()
    section1 = sections[0]
    option = 'category'
    value = 'testing'
    print 'adding -- section: "%s"  option: "%s"  value: "%s"' % (
        section1, option, value, )
    parser.set(section1, option, value)


def test(in_config_file_name, out_config_file_name):
    parser = ConfigParser()
    #print 'parser:', parser
    parser.read([in_config_file_name])
    print_report(parser)
    print '-' * 40
    add_items(parser)
    if os.path.exists(out_config_file_name):
        print '\n*\n*** output file exists.  skipping write.\n*\n'
    else:
        out_config_file = open(out_config_file_name, 'w')
        parser.write(out_config_file)
        out_config_file.close()
    table = construct_table(parser)
    print '-' * 40
    print 'Table --'
    pp = pprint.PrettyPrinter(indent=4)
    print pp.pformat(table)
    #print '-' * 40
    #print 'general/category: %s' % table['details']['category']


def main():
    args = sys.argv[1:]
    if len(args) != 2:
        print 'usage: python config_report.py in_config.ini out_config.ini'
        sys.exit(1)
    test(args[0], args[1])

if __name__ == '__main__':
    main()
