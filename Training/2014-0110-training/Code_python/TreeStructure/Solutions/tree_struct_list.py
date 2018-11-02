#!/usr/bin/env python

"""
Create and walk a tree structure composed of lists.
"""

Version = 'version 1.0a'

def show(node, indent):
    if node is not None:
        print '%s%s' % (indent, node[0], )
        indent += '    '
        show(node[1], indent)
        show(node[2], indent)

def test():
    n1 = ['black oak', None, None]
    n2 = ['white oak', None, None]
    n3 = ['oak', n1, n2]
    show(n3, '')

if __name__ == '__main__':
    test()

