#!/usr/bin/env python

"""
Sample code for creating and using class methods and static methods.
"""

import types


class SomeClass(object):

    def __init__(self, name):
        self.name = name

    def show(self):
        print 'SomeClass -- name: "%s"' % self.name

    @classmethod
    def HelloClass(cls, arg):
        print 'Hello from class method'
        print '    cls:', cls
        print '    arg:', arg
    #HelloClass = classmethod(HelloClass)

    @staticmethod
    def HelloStatic(arg):
        print 'Hello from static method'
        print '    arg:', arg
    #HelloStatic = staticmethod(HelloStatic)

    @classmethod
    def from_name(cls, name):
        obj = cls(name)
        return obj
    #from_name = classmethod(from_name)

    @classmethod
    def from_integer(cls, size):
        if not isinstance(size, types.IntType):
            raise TypeError('from_integer requires integer arg')
        if size == 1:
            csize = 'one'
        elif size == 2:
            csize = 'two'
        elif size == 3:
            csize = 'three'
        else:
            csize = 'big'
        obj = cls(csize)
        return obj
    #from_integer = classmethod(from_integer)


class SomeSubClass(SomeClass):
    def show(self):
        print 'SomeSubClass -- name: "%s"' % self.name


def test():
    SomeClass.HelloClass('abcd')
    SomeClass.HelloStatic('efgh')
    obj = SomeClass.from_name('dave')
    obj.show()
    obj = SomeClass.from_integer(2)
    obj.show()
    obj = SomeSubClass.from_name('sylvia')
    obj.show()
    obj = SomeSubClass.from_integer(4)
    obj.show()
    #obj = SomeClass.from_integer(2.0)


if __name__ == '__main__':
    test()
