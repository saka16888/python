#!/usr/bin/env python

"""
This module provides code samples that can
demonstrate the (order of) evaluation and execution of Python code.

A few notes:

- Python executes statements from the top of the module to the
  bottom.
- Some statements result in the binding of a value to a name
  within the current namespace.  Examples are assignment,
  function definition (def), class definition (class),
  and module import (import).  Function/method call also
  binds values to arguments (within the function body).
- Expressions within a statement are evaluated to produce a value
  See notes on operators for more on expression evaluation.
- Statements within a function definition are executed when the
  function is called, *not* when the function is defined.
- At any given level, there is only one namespace.  For example,
  functions, classes, and data variables are in the same namespace.
  So, for example, it is not possible to have a function and
  a data variable with the same name in a single namespace.
"""

#
# Imports:
import sys
import os


#
# Global variables and constants:

STANDARD_COLOR = 'blue'


#
# Functions for external use, factories, etc:

def make_music_lover(name):
    p = MusicLover(name)
    return p


#
# Duplicate name.  Teaching point only.
def make_music_lover(name):
    p = OperaLover(name)
    return p


#
# Classes:

class MusicLover(object):
    def __init__(self, name):
        self.name = name
    def show(self):
        pass


class OperaLover(MusicLover):
    def __init__(self, name, favorites):
        MusicLover.__init__(self, name)
        self.favorites = favorites
    def show(self):
        pass
    def get_favorite_opera(self):
        return self.favorites[0]


class RockAndRollLover(MusicLover):
    pass


#
# Functons for internal use:

def test(arg1):
    """A test function.  Replace with your code.
    """
    print 'This is a test.  arg1:', arg1
    f = another_test1
    f()
    another_test2()
    idx = 0
    if idx >= 0:
        f = FUNCTIONS[idx + 1]
        f()

#
# Run the code.  Teaching point only.
# Should produce an error, because another_test and FUNCTIONS are
#   not yet defined.
#
#test('abcd')


def another_test1():
    print 'another_test1'

def another_test2():
    print 'another_test2'
    # Generate an error.  Show a sample trace-back.
    #x = zzz


#
# Teaching point only.  Usually define globals near top of module.
FUNCTIONS = [another_test1, another_test2, ]


def usage():
    print 'Usage: ...'
    sys.exit(-1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    test(args[0])


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

