#!/usr/bin/env python

"""
Create and use simple objects.

1. Define a simple class.
2. Call a function to create an instance of the class.
3. Call a method in that object.
"""


class A(object):

    def __init__(self, name):
        self.name = name

    def calc(self, x):
        return x * 3


class B(A):
    def __init__(self, name, size):
        super(B, self).__init__(name)
        self.size = size

    def show(self):
        print 'name:', self.name, 'size:', self.size


def make_object():
    b = B('gladiola', 35)
    return b


def test():
    obj = make_object()
    obj.show()

if __name__ == '__main__':
    test()
