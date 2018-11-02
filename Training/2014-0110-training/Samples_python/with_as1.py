#!/usr/bin/env python

"""
Provide an example of the "with/as:" and a context manager object.

A context manager object is an instance of a class that implements
the context management protocol.
"""


from __future__ import with_statement
import traceback


class ContextManager(object):
    def __init__(self, name):
        self.name = name
    def show(self, msg):
        print 'showing -- name: %s  msg: "%s"' % (self.name, msg, )
    def __enter__(self):
        print '(__enter__)'
        return self
    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            print '(__exit__) normal exit'
        else:
            print '-' * 40
            traceback.print_tb(exc_tb)
            print '-' * 40
            traceback.print_exception(exc_type, exc_value, exc_tb)
            print '-' * 40
            self.show_tb(exc_tb)
            print '-' * 40
            print '(__exit__) exc_type: %s  exc_value: %s  exc_tb: %s' % (
                exc_type, exc_value, exc_tb, )
            # To propagate (bubble up) the exception, return a False value.
            return True
    def show_tb(self, tb):
        #print dir(tb)
        while tb:
            print 'lineno: %d  frame: %s' % (tb.tb_lineno, tb.tb_frame, )
            #print dir(tb.tb_frame)
            tb = tb.tb_next

def test_contextmanger():
    #raise RuntimeError, 'Testing traceback'
    with ContextManager('Test1') as context:
        context.show('Test #1')
        print 'finishing ok'
    with ContextManager('Test2') as context:
        context.show('Test #2  before')
        raise RuntimeError, 'Testing the context manager'
        context.show('Test #2  after')
        print 'not finished'

def test():
    test_contextmanger()

if __name__ == '__main__':
    test()
