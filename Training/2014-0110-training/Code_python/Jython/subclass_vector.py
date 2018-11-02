
"""
Test implementing a subclass of a Java class.

Usage: jython test_vector_subclass.py arg1 arg2 ...
"""

import sys
import types
from java.util import Vector


#
# is-a
# UpperVector is a Vector.
class UpperVector(Vector):
    def __init__(self, newvector=None):
        if newvector is None:
            newvector = []
        for item in newvector:
            if type(item) is not types.StringType:
                raise RuntimeError, 'Can only add strings, not: %s' % item
        Vector.__init__(self, newvector)
    def upperElementAt(self, idx):
        #s1 = self.elementAt(idx)
        s1 = Vector.elementAt(self, idx)
        s1 = s1.upper()
        return s1
    def elementAt(self, idx):
        s1 = Vector.elementAt(self, idx)
        s1 = '[[%s]]' % s1
        return s1
    def add(self, newobj):
        if type(newobj) is not types.StringType:
            raise RuntimeError, 'Can only add strings, not: %s' % newobj
        Vector.add(self, newobj)

#
# has-a
# OtherUpperVector has a Vector.
class OtherUpperVector(object):
    def __init__(self, newlist):
        self.vect = Vector(newlist)
    def elementAt(self, idx):
        pass


def test():
    args = sys.argv[1:]
    if len(args) < 2:
        print __doc__
        sys.exit(1)
    uv1 = UpperVector()
##     uv1.add('abc')
##     uv1.add('def')
    for arg in args:
        uv1.add(arg)
    print uv1.upperElementAt(0)
    print uv1.upperElementAt(1)
    print uv1.elementAt(0)
    print uv1.elementAt(1)
    uv2 = UpperVector(['the', 'pretty', 'kittie'])
    print uv2.upperElementAt(1)
    uv3 = UpperVector([1, 2, 3])


if __name__ == '__main__':
    test()

