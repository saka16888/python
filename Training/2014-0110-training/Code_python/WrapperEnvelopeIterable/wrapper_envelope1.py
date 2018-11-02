#!/usr/bin/env python

"""
Wrap (subclass) the ConfigParser in an iterable class.
"""

#
# Imports:
import sys
from ConfigParser import ConfigParser


#
# Global variables and constants:



#
# Functions for external use, factories, etc:

def make_iterator(infilename):
    iter1 = IterableConfigParser(infilename)
    return iter1


#
# Classes:

class IterableConfigParser(object):
    def __init__(self, infilename):
        self.parser = ConfigParser()
        self.parser.read(infilename)
        self.sections = self.parser.sections()
        self.items = []
        for section in self.sections:
            options = self.parser.options(section)
            for option in options:
                self.items.append((section, option))
        self.item_iter = iter(self.items)
    def __iter__(self):
        return self
    def next(self):
        section, option = self.item_iter.next()
        value = self.parser.get(section, option)
        return section, option, value
            


#
# Functons for internal use:

def test(infilename):
    """Test the IterableConfigParser.
    """
    parser = make_iterator(infilename)
    print parser.items
    for section, option, value in parser:
        print '%s/%s: %s' % (section, option, value, )


def usage():
    print 'Usage: python wrapper_envelope1.py infilename'
    sys.exit(-1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    test(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

