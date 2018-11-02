#!/usr/bin/env python

import sys
import re

def re_match01(pattern, infilename):
    found = []
    with open(infilename, 'r') as infile:
        for line in infile:
            line = line.strip()
            target = extract(pattern, line)
            if target is not None:
                found.append((target, line))
    found.sort()
    # sort by line, not target
    #found.sort(key=lambda x: x[1])
    for target, line in found:
        print('%s::%s' % (target, line))


def extract(pattern, line):
    target = None
    match_obj = re.search(pattern, line)
    if match_obj is not None:
        target = match_obj.group(1)
    return target

def main():
    args = sys.argv[1:]
    if len(args) != 2:
        sys.exit(
            "\nusage: python unique_lines01.py <pattern> <in_file_name>\n")
    pattern = args[0]
    infilename = args[1]
    re_match01(pattern, infilename)

if __name__ == '__main__':
    #import ipdb; ipdb.set_trace()
    main()
