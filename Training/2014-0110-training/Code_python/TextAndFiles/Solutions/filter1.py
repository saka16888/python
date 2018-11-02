#!/usr/bin/env python


"""
Demonstrate text filter functions, polymorphism, and string operations.

Provide sample code for the following:
- Text filter functions -- pass function as argument to a function.
- Polymorphism -- Ability to interchangably use functions.
- String transformation and formatting

"""

import sys

#
# Filter/transformation functions that each operate on a single line.
#


# A do nothing filter.
def filter_null(line):
    return line


# Convert line to all uppercase.
def filter_toupper(line):
    line = line.upper()
    return line


# Add comment characters at beginning of line.
def filter_tocomment(line):
    line = '## %s' % (line, )
    return line


# Remove comment characters at beginning of line.
def filter_touncomment(line):
    if line.startswith('## '):
        line = line[3:]
    return line


# Do a simple (fixed) string replacement.
## def filter_repl(line):
##     return line.replace('filter', 'transform')

# Return only non-empty, non-whitespace lines.
def filter_nonwhitespaceonly(line):
    if len(line.strip()) > 0:
        return line
    else:
        return None


# Implement a closure that does a simple (fixed) string replacement.
# The closure captures the target and replacement from the outer function.
def filter_repl(target, repl):
    def inner(line):
        return line.replace(target, repl)
    return inner


#
# The main driver function.
# Read stdin and write to stdout.  Pass each line through filter_func.
def filter(filter_func):
    for line in sys.stdin:
        line = filter_func(line)
        if line is not None:
            sys.stdout.write(line)


def main():
    #filter(filter_nonwhitespaceonly)
    func = filter_repl('filter', 'transform')
    filter(func)

if __name__ == '__main__':
    main()
