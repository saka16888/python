"""
Synopsis:
    Search a target string for a pattern.
    Print all the positions of the occurance of the pattern string
        within the target string.
    Implement the above in two different ways:
        1. Use a while: statement.
        2. Implement a generator function (a function that uses the
           yield statement).
Usage:
    python search_str.py
"""

import sys


def search_while(pat, target):
    pos = 0
    while True:
        pos = target.find(pat, pos)
        if pos < 0:
            break
        print pos
        pos += 1


def generate_positions(pat, target):
    pos = 0
    while True:
        pos = target.find(pat, pos)
        if pos < 0:
            break
        yield pos
        pos += 1


def test():
    args = sys.argv[1:]
    if len(args) != 0:
        sys.exit(__doc__)
    search_while('xxx', 'aaaxxxbbbxxxcccxxxdddxxxeee')
    print '=-' * 30
    generator1 = generate_positions('xxx', 'aaaxxxbbbxxxcccxxxdddxxxeee')
    for pos in generator1:
        print 'pos:', pos


if __name__ == '__main__':
    test()
