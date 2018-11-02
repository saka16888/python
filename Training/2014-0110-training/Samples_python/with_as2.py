import sys
import time


class SimpleContext(object):
    """A simple context manager"""
    def __init__(self, label):
        self.label = label

    def __enter__(self):
        print "entering block"
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            print "leaving block"
        else:
            sys.stderr.write("caught exception -- type: %s\n" % (exc_type, ))
            # return False to propagate the exception up the call stack.
            # return True to end exception processing.
            return False

    def print_msg(self, msg, outfile=sys.stdout):
        outfile.write("%s (%s) %s\n" % (self.label, time.ctime(), msg, ))


def test_with():
    print 'stage 1'
    with SimpleContext('logging 1') as context:
        context.print_msg('message 1')
        context.print_msg('message 2')
        context.print_msg('message 3')
        context.label = 'logging 2'
        context.print_msg('message 4')
        context.print_msg('message 5')
        context.print_msg('message 6')
    print 'stage 2'
    with SimpleContext('logging 3') as context:
        context.print_msg('message 7')
        # cause a NameError exception
        print unknown_variable
        context.print_msg('message 8')
    print 'stage 3'


def test():
    try:
        test_with()
    except NameError as exp:
        print 'caught exception up above -- exp: %s' % exp


test()
