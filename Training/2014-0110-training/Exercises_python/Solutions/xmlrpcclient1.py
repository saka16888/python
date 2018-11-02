#!/usr/bin/python

"""
Synopsis:
    Implement an XML-RPC client that "calls" the functions provided by
        your XML-RPC server.
Usage:
    python xmlrpcclient1.py
Hints:
    - module SimpleXMLRPCServer in the Python standard library.
    - module xmlrpclib in the Python standard library.
Solution:
    Solutions/xmlrpcclient1.py
"""

import xmlrpclib


def test():
    s = xmlrpclib.ServerProxy('http://localhost:8000')
    print 'pow(2, 3) --', s.pow(2, 3)  # Returns 2**3 = 8
    print 'add(2, 3) --', s.add(2, 3)  # Returns 5
    print 'div(5, 2) --', s.div(5, 2)  # Returns 5//2 = 2
    # Print list of available methods
    print s.system.listMethods()


if __name__ == '__main__':
    test()
