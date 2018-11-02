#!/usr/bin/env python

"""This is a template for a Python module.

This template supports command line arguments and
command line flags.

This template also contains a sample of a simple class definition.

Copy, modify, and add to this module until it does something
you want it to do.
"""

import sys
import getopt


class MySimpleClass(object):
    """This is a simple template for a Python class.
    """
    def __init__(self, name='nobody'):
        self.name = name

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def show(self):
        print "Hello, I'm %s" % (self.name, )


def test(verbose, avalue):
    """Modify or replace this function for your own needs.
    """
    print 'verbose: %s  avalue: %s' % (verbose, avalue, )
    obj = MySimpleClass('MySimpleClass')
    obj.show()
    if avalue:
        obj.set_name(avalue)
    obj.show()


USAGE_TEXT = """
Usage:
    python ???.py [options] [arg ...]
Options:
    -h, --help      Display this help message.
    -a, --avalue    A test value.
    -v, --verbose   Verbose -- Print extra info.
Example:
    python ???.py ???
"""


def usage():
    print USAGE_TEXT
    sys.exit(1)


def main():
    args = sys.argv[1:]
    try:
        opts, args = getopt.getopt(args, 'hva:', [
            'help', 'verbose', 'avalue=', ])
    except:
        usage()
    verbose = False
    avalue = None
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt in ('-v', '--verbose'):
            verbose = True
        elif opt in ('-a', '--avalue'):
            avalue = val
    if len(args) != 0:
        usage()
    test(verbose, avalue)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
