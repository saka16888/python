#!/usr/bin/env python
"""
Read from stdin and write to stdout.
Convert output: add "## ".
"""

import sys


def convert():
    for line in sys.stdin:
        line = '## %s' % line
        sys.stdout.write(line)


if __name__ == '__main__':
    convert()
