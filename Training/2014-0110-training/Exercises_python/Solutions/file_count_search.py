#!/usr/bin/env python
"""
Synopsis:
    1. Process all the files whose names match a path/pattern.  For
       each file, do the following -- Count the characters, the
       words, and the lines in the file.  Print these counts.
       ``glob``.
    2. Process all the files whose names match a path/pattern.  For
       each file, do the following -- Search each line for a
       pattern.  Print each line that matches.
Usage:
    python file_count_search.py count <file_name_pattern>
    python file_count_search.py search <text_pattern> <file_name_pattern>
Hints:
    - glob module in the Python standard library
    - re (regular expression) module in the Python standard library
"""

import sys
import re
import glob


def count(pattern):
    filenames = glob.glob(pattern)
    for filename in filenames:
        char_count = 0
        word_count = 0
        line_count = 0
        with open(filename, 'r') as infile:
            for line in infile:
                #line = line.rstrip('\n')
                char_count += len(line)
                word_count += len(re.split(r'\W+', line))
                line_count += 1
        print '%s -- chars: %d  words: %d  lines: %d' % (
            filename,
            char_count, word_count, line_count, )


def search(text_pattern, file_pattern):
    ctext_pattern = re.compile(text_pattern)
    file_names = glob.glob(file_pattern)
    file_names.sort()
    for file_name in file_names:
        with open(file_name, 'r') as infile:
            line_no = 0
            for line in infile:
                line_no += 1
                line = line.rstrip()
                match_object = ctext_pattern.search(line)
                if match_object is not None:
                    print '%s:%d:%s' % (file_name, line_no, line, )


def main():
    args = sys.argv[1:]
    if len(args) < 2:
        sys.exit(__doc__)
    if args[0] == 'count':
        count(args[1])
    elif args[0] == 'search':
        search(args[1], args[2])
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main()
