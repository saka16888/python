#!/usr/bin/env python


"""
Filters using generator functions.

Use generator functions to write filters.
Each filter function takes the following arguments:
  1. An iterable
  2. A function that returns the line filtered or None if the item
     is to be skipped.
Each filter function returns a generator (because the function
contains yield).
"""


def isiterable(x):
    """Return True if the arg is iterable.
    """
    try:
        iter(x)
    except TypeError:
        return False
    return True


def filter(iterable, filter_func):
    """Filter the strings in iterable using filter_func.

    Return a generator function.
    """
    for item in iterable:
        item = filter_func(item)
        if item is not None:
            yield item


def add_double_mash(line):
    """Add comment characters ("## ") to the start of the line.
    """
    return '## %s' % line


def rstrip_line(line):
    """Strip whitespace off the right end of the line.
    """
    return line.rstrip()


def skip_if_emptystring(line):
    """Return None if the line is empty of contains only whitespace.
    """
    if line.isspace():
        return None
    else:
        return line


def test():
    """Run a test of this module.
    """
    # Separate generator objects.
    infilename = 'filter2.py'
    infile = open(infilename, 'r')
    g1 = filter(infile, skip_if_emptystring)
    g2 = filter(g1, add_double_mash)
    g3 = filter(g2, rstrip_line)
    for line in g3:
        print line
    infile.close()
    # Nested calls to generator functions.
    print '-' * 50
    infile = open(infilename, 'r')
    for line in filter(
            filter(
                filter(infile, skip_if_emptystring),
                add_double_mash),
            rstrip_line):
        print line
    infile.close()


if __name__ == '__main__':
    test()
