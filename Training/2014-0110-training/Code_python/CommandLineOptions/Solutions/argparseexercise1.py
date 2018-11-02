#!/usr/bin/env python

import argparse


def test(args):
    print 'count: %d  %s' % (args.count, type(args.count), )
    print 'verbose: %s  %s' % (args.verbose, type(args.verbose), )
    print 'arg1: %d  %s' % (args.arg1, type(args.arg1), )
    print 'arg2: "%s"  %s' % (args.arg2, type(args.arg2), )


def main():
    parser = argparse.ArgumentParser(description='A simple test for argparse')
    parser.add_argument(
        '-v', '--verbose', action='store_true', dest='verbose',
        help='Print additional information'
    )
    parser.add_argument(
        '-c', '--count', type=int, dest='count',
        help='The number of repetitions'
    )
    parser.add_argument(
        type=int, dest='arg1',
        help='Argument 1 -- an integer'
    )
    parser.add_argument(
        type=str, dest='arg2',
        help='Argument 2 -- a string'
    )
    args = parser.parse_args()
    test(args)


if __name__ == '__main__':
    main()
