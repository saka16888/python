#!/usr/bin/env python

"""
Define an exception class, then raise and catch exceptions of that type.

To cause an exception, use a command line option other than -h, -f,
    --help, or --force.
"""

import sys
import getopt


class MyException(Exception):
    pass


def deep_error(args):
    print '(deep_error) before error'
    deep_deep_error(args)
    print '(deep_error) after error'


def other_deep_error(args):
    print '(deep_error) before error'
    deep_deep_error(args)
    print '(deep_error) after error'


def deep_deep_error(args):
    """Teaching point -- Enter bad option to generate error.

    Note that deep_deep_error is called from two locations.
    """
    #
    # Teaching point: raise a user defined exception.
    #raise MyException('a simple error message')

    options, args = getopt.getopt(
        args, 'hf',
        ['help', 'force', ])


def shallow_error():
    print '(shallow_error) before error'
    x = y + 3
    print '(shallow_error) after error'


def main():
    args = sys.argv[1:]
    #shallow_error(args)
    #shallow_error()
    deep_error(args)


if __name__ == '__main__':
    main()
