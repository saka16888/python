#!/usr/bin/env python


"""
Print a report of sections and options in a config file.
"""

import sys
from ConfigParser import ConfigParser

def report(config_file_name):
    parser = ConfigParser()
    parser.read(['config1.ini'])
    sections = parser.sections()
    for section in sections:
        options = parser.options(section)
        for option in options:
            value = parser.get(section, option)
            print '%s:%s: %s' % (section, option, value, )

def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print 'usage: jython config_report.py in_config.ini'
        sys.exit(1)
    config_file_name = args[0]
    report(config_file_name)

if __name__ == '__main__':
    main()

