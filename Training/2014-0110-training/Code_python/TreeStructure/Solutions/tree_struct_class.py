#!/usr/bin/env python

"""
Create and walk a binary tree structure.  Nodes are instances of class Node.
"""

Version = 'version 1.0a'


class Tree(object):
    def __init__(self, val, left_child, right_child):
        self.val = val
        self.left_child = left_child
        self.right_child = right_child

    def show(self, level):
        print '%sval: %s' % (level, self.val, )
        level += '    '
        if self.left_child is not None:
            self.left_child.show(level)
        if self.right_child is not None:
            self.right_child.show(level)


def test():
    n1 = Tree('black oak', None, None)
    n2 = Tree('white oak', None, None)
    n3 = Tree('oak', n1, n2)
    n3.show('')

if __name__ == '__main__':
    test()
