#!/usr/bin/env python

"""
Sample use of getopt module to capture command line arguments.

Usage:
    python getoptexample1.py [options] [arg ...]
Options:
    -h, --help      Display this help message.
    -c, --count     A integer value.
    -v, --verbose   Verbose -- Print extra info.
Arguments -- Any number of arguments (but at least one).
Example:
    python getoptexample1.py -v -c abc def ghi
    python getoptexample1.py --verbose --count="aaa bbb ccc" ddd eee fff
"""


import sys
import getopt


def test(verbose, count, args):
    """Display the options and arguments from the command line.
    """
    print 'verbose: %s  count: %s' % (verbose, count, )
    print 'args:', args


def usage():
    print __doc__
    sys.exit(1)


def main():
    args = sys.argv[1:]
    try:
        opts, args = getopt.getopt(args, 'hvc:', [
            'help', 'verbose', 'count=', ])
    except:
        usage()
    verbose = False
    count = None
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt in ('-v', '--verbose'):
            verbose = True
        elif opt in ('-c', '--count'):
            try:
                count = int(val)
            except ValueError:
                sys.exit('count must be integer, not "%s"\n' % val)
                #sys.exit(1)
    if len(args) < 1:
        usage()
    test(verbose, count, args)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
