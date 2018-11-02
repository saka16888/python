#!/usr/bin/env python

"""
Synopsis:
    Recursively print out the names of files and directories starting
    at a given path.
Usage:
    python report_files_directories.py <path>
Hints:
    - glob module in the Python standard library
    - os.path.isdir function
"""

import sys
import os
import glob


def walk(path):
    names = glob.glob(os.path.join(path, '*'))
    for name in names:
        if os.path.isdir(name):
            print 'directory:', name
            walk(name)
        else:
            print 'file:', name


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        sys.exit(__doc__)
    walk(args[0])


if __name__ == '__main__':
    main()
