#!/usr/bin/env python

"""This is a template for a Python module.

This template supports command line arguments but *not*
command line flags.

Copy, modify, and add to this module until it does something
you want it to do.
"""

import sys


def test(arg1):
    """A test function.  Replace with your code.
    """
    print 'This is a test.  arg1:', arg1


def usage():
    print 'Usage: ...'
    sys.exit(-1)


# alternative usage function
def usage1():
    # Put the usage string in the doc string for this module.
    print __doc__
    sys.exit(-1)


# another alternative
# sys.exit(some_string) prints the string *and* exits the program.
def usage2():
    sys.exit(__doc__)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    test(args[0])


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
