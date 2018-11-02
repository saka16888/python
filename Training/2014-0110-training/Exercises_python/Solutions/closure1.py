#!/usr/bin/env python

"""
Synopsis:
    You need to implement a function that takes 1 argument, but you
        need a way to give that function an additional parameter.
    Create a closure.
    Implement a function that takes 1 argument, but has an additional
        argument "packed" into it.
Usage:
    python closure1.py infilename
Options:
    -h, --help      Display this help message.
Example:
    python elementtree_walk.py myxmldoc.xml
Hints:
    - Write a nested function definition.
Solution:
    Solutions/closure1.py
"""


#
# This function takes as an argument a function that takes exactly one
#     argument.  But, we need to give it 2 values.
def process(fn, data):
    for item in data:
        fn(item)


#
# Create a function that takes one argument, but that has another value
#     packed into it.
def makefn(name):
    def innerfn(item):
        print name, item
    return innerfn


def test():
    data = ['arugula', 'broccoli', 'cauliflower', ]
    fn = makefn('stir fry')
    process(fn, data)
    fn = makefn('sautee')
    process(fn, data)
    fn = makefn('pan fry')
    process(fn, data)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    test()
