#!/usr/bin/env python
"""
A sample process that can be used to test use of the subprocess module.
See file subprocess_test01.py for an example.
"""

import sys


def pipe():
    content = sys.stdin.read()
    content = content.upper()
    sys.stdout.write(content)


if __name__ == '__main__':
    pipe()
