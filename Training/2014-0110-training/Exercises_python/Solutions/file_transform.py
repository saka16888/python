#!/usr/bin/env python

import sys


def transform():
    for line in sys.stdin:
        line = '## %s' % line
        sys.stdout.write(line)


if __name__ == '__main__':
    transform()
