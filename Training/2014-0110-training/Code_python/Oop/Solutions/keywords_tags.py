#!/usr/bin/env python

"""
Implement a basic (tree) Node class and a keyword annotated tree.

Implement a basic node class that has the following instance
variables:

- ``value`` -- a string

- ``keywords`` -- a list of strings

- ``children`` -- a list of child nodes

"""

import sys


class Node(object):
    """
    A node in a keyword annotated tree.

    A node has a value, a list of keywords, and a list of children.
    """
    def __init__(self, value, children=None, keywords=None):
        self.value = value
        if children is None:
            self.children = []
        else:
            self.children = children
        if keywords is None:
            self.keywords = []
        else:
            self.keywords = keywords

    def show(self, level):
        """Show a node indented to level.
        """
        self.showlevel(level)
        print 'value: "%s"  keywords: "%s"' % (self.value, self.keywords, )
        level += '    '
        for child in self.children:
            child.show(level)

    def collect(self, index):
        """Walk this node and children collecting keywords in a dictionary.
        """
        for keyword in self.keywords:
            keyword = keyword.lower()
            if keyword in index:
                index[keyword].append(self)
            else:
                index[keyword] = [self]
        for child in self.children:
            child.collect(index)

    def showlevel(self, level):
        sys.stdout.write(level)

    def __str__(self):
        return '<Node %s %s>' % (self.value, self.keywords, )
    __repr__ = __str__


def test():
    n1 = Node('dave', keywords=['programming', 'birding', ])
    n2 = Node('mona', keywords=['birding', 'gardening', ])
    n3 = Node('abrigail', [n1, n2, ])
    n3.show('')
    index = {}
    n3.collect(index)
    print '-' * 60
    print 'index:'
    for keyword, nodes in index.items():
        print '    %s:' % (keyword, )
        for node in nodes:
            print '        %s' % (node, )


if __name__ == '__main__':
    test()
