#!/usr/bin/env python

"""
Create and use several objects.
"""


class LittleObj(object):
    address = 'xxx@yyy.com'

    def __init__(self, name='<nobody>'):
        self.name = name

    def set_name(self, name):
        self._validate(name)
        self.name = name

    def show(self):
        print 'hello from a LittleObj.  My name is: %s' % self.name

    def shift(self):
        self.name = self.name.upper()

    def _validate(self):
        pass


class SpecialLittleObj(LittleObj):
    def __init__(self, name, description):
        #LittleObj.__init__(self, name)
        super(SpecialLittleObj, self). __init__(name)
        self.description = description

    def show(self):
        LittleObj.show(self)
        print '    description: "%s"' % (self.description, )


def test():
    obj1 = LittleObj('dave')
    obj2 = LittleObj('joe')
    obj1.show()
    obj2.show()
    obj2.shift()
    obj2.show()
    obj2.name = 'luis'
    obj2.show()
    obj3 = SpecialLittleObj('peggy', 'today is sunny and cold')
    obj3.show()

if __name__ == '__main__':
    test()
