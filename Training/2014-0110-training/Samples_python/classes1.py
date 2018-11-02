#!/usr/bin/env python

"""
Samples of basic Python class definitions.
"""

import sys


class Simple(object):
    """A pathetically simple class.

    A class with no implementation can be used as a
    record with arbitrary named "fields".
    """
    pass


def test_simple():
    obj1 = Simple()
    obj1.x = 12
    obj1.y = 15
    print 'x: %d  y: %d' % (obj1.x, obj1.y, )


class Tree(object):
    """A tree in the forest or the park or ...

    A Tree knows its name and size.
    It can also show itself.
    """
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size

    def show(self):
        print 'Tree -- name: "%s"  size: %d' % (
            self.name, self.size, )


def test_trees():
    obj2 = Tree('jeffery pine', 125)
    print 'obj2 -- name: "%s"  size: %d' % (
        obj2.get_name(), obj2.get_size(), )
    obj2.set_size(140)
    print 'obj2 -- name: "%s"  size: %d' % (
        obj2.get_name(), obj2.get_size(), )
    obj2.show()


class DeciduousTree(Tree):
    """A deciduous tree.

    Adds leaf_shape to the capabilities of the superclass Tree.
    """
    def __init__(self, name, size, leaf_shape):
        Tree.__init__(self, name, size)
        self.leaf_shape = leaf_shape

    def set_leaf_shape(self, leaf_shape):
        self.leaf_shape = leaf_shape

    def get_leaf_shape(self):
        return self.leaf_shape

    def show(self):
        Tree.show(self)
        print 'DeciduousTree -- leaf_shape: "%s"' % (
            self.leaf_shape, )


def test_deciduous_tree():
    oak1 = DeciduousTree('Valley oak (Quercus lobata)', 90, 'lobed')
    oak1.show()


class Link(object):
    """A link/node in a single linked list.

    A link has a name and a next link (or None).
    """
    def __init__(self, name='<null>', next=None):
        self.name = name
        self.next = next

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next


def test_singlelinkedlist():
    link1 = None
    for idx in range(5):
        name = 'somelink%d' % (idx + 1, )
        link1 = Link(name, link1)
    link2 = link1
    count = 0
    while link2:
        count += 1
        print '%d.  name: "%s"' % (count, link2.get_name(), )
        link2 = link2.get_next()


class BinaryNode(object):
    """Represent a node in a tree data structure.

    A Node has a value (data) and two children (lchild and rchild).
    """
    def __init__(self, value='[empty]', lchild=None, rchild=None):
        self.value = value
        self.lchild = lchild
        self.rchild = rchild

    def show(self, level):
        self.show_indent(level)
        print 'value: "%s"' % (self.value, )
        if self.lchild is not None:
            self.lchild.show(level + 1)
        if self.rchild is not None:
            self.rchild.show(level + 1)

    def show_indent(self, level):
        size = level * 4
        s1 = ' ' * size
        sys.stdout.write(s1)


def test_binary_tree_structure():
    n8 = BinaryNode('value8')
    n7 = BinaryNode('value7')
    #n6 = BinaryNode('value6')
    n5 = BinaryNode('value5')
    n4 = BinaryNode('value4')
    n3 = BinaryNode('value3', n7, n8)
    n2 = BinaryNode('value2', n4, n5)
    n1 = BinaryNode('value1', n2, n3)
    n1.show(0)


class Node(object):
    """Represent a node in a tree data structure.

    A Node has a value (data) and a list of children.
    """
    def __init__(self, value='[empty]', children=None):
        self.value = value
        if children is None:
            self.children = []
        else:
            self.children = children

    def show(self, level):
        self.show_indent(level)
        print 'value: "%s"' % (self.value, )
        for child in self.children:
            child.show(level + 1)

    def show_indent(self, level):
        size = level * 4
        s1 = ' ' * size
        sys.stdout.write(s1)


def test_tree_structure():
    n8 = Node('value8')
    n7 = Node('value7')
    n6 = Node('value6')
    n5 = Node('value5')
    n4 = Node('value4')
    n3 = Node('value3', [n7, n8, ])
    n2 = Node('value2', [n4, n5, n6, ])
    n1 = Node('value1', [n2, n3, ])
    n1.show(0)


def hr(msg):
    """Print a horizontal rule and a title/message.
    """
    print '-' * 60
    print msg
    print '-' * len(msg)


def test():
    hr('Simple class:')
    test_simple()
    hr('Trees:')
    test_trees()
    hr('Sub-class (DeciduousTree):')
    test_deciduous_tree()
    hr('Single-linked list:')
    test_singlelinkedlist()
    hr('Binary tree data structure:')
    test_binary_tree_structure()
    hr('Tree (multiple children) data structure:')
    test_tree_structure()


if __name__ == '__main__':
    test()
