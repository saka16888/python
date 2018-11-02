#!/usr/bin/env python

import sys

def unique01(filename):
    infile = open(filename, 'r')
    unique_ids = set()
    for line in infile:
        line = line.strip()
        if line:
            id = line[:6]
            if id not in unique_ids:
                unique_ids.add(id)
                print(line)
    infile.close()

def unique02(filename):
    unique_ids = set()
    with open(filename, 'r') as infile:
        for line in infile:
            line = line.strip()
            if line:
                id = line[:6]
                if id not in unique_ids:
                    unique_ids.add(id)
                    print(line)

def unique03(filename):
    infile = open(filename, 'r')
    unique_ids = set()
    lines = infile.readlines()
    lines.reverse()
    for line in lines:
        line = line.strip()
        if line:
            id = line[:6]
            if id not in unique_ids:
                unique_ids.add(id)
                print(line)
    infile.close()


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        sys.exit("\nusage: python unique_lines01.py <in_file_name>\n")
    unique03(args[0])

if __name__ == '__main__':
    main()
