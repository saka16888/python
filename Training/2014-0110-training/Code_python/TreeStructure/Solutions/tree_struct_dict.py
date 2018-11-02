#!/usr/bin/env python

"""
Create and walk a tree structure composed of dictionaries.
"""


Version = 'version 1.0a'

Node1 = {'name': 'black oak', 'lsib': None, 'rsib': None}
Node2 = {'name': 'white oak', 'lsib': None, 'rsib': None}
Node3 = {
    'name': 'oak',
    'lsib': Node1,
    'rsib': Node2,
}

Node = {
    'name': 'oak',
    'lsib': {
        'name': 'black oak',
        'lsib': None,
        'rsib': None,
    },
    'rsib': {
        'name': 'white oak',
        'lsib': None,
        'rsib': None,
    },
}


def show(node, indent):
    if node is not None:
        print '%s%s' % (indent, node['name'], )
        indent += '    '
        show(node['lsib'], indent)
        show(node['rsib'], indent)


def test():
    n1 = {'name': 'black oak', 'lsib': None, 'rsib': None}
    n2 = {'name': 'white oak', 'lsib': None, 'rsib': None}
    n3 = {'name': 'oak', 'lsib': n1, 'rsib': n2}
    show(n3, '')
    show(Node3, '')
    show(Node, '')

if __name__ == '__main__':
    test()
