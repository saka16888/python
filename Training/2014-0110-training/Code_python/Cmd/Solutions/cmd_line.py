#!/usr/bin/env python

"""
Sample of the use of the cmd module to create a command line user interface.
"""


#
# Imports:
import sys
import getopt
from cmd import Cmd


#
# Global variables and constants:



#
# Functions for external use, factories, etc:



#
# Classes:

class CmdLine(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = 'Enter cmd: '

    do_h = Cmd.do_help

    def do_hello(self, args):
        """Say hello and display any arguments.
        """
        print 'hello'
        args = args.split()
        for arg in args:
            print '    arg: "%s"' % (arg, )
        return False

    def emptyline(self):
        pass

    def do_quit(self, args):
        """Say goodbye and quit.
        """
        print 'bye'
        # Return True in order to exit from the command loop.
        return True
    do_exit = do_quit


#
# Functions for internal use:

def test():
    """Test the CmdLine object.
    """
    cmdline = CmdLine()
    cmdline.cmdloop('Welcome to the command line.')
    


USAGE_TEXT = """
Usage:
    python ???.py [options] [arg ...]
Options:
    -h, --help      Display this help message.
    -a, --avalue    A test value.
    -v, --verbose   Verbose -- Print extra info.
Example:
    python ???.py ???
"""

def usage():
    print USAGE_TEXT
    sys.exit(1)


def main():
    args = sys.argv[1:]
    try:
        opts, args = getopt.getopt(args, 'h', ['help',
            ])
    except:
        usage()
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
    if len(args) != 0:
        usage()
    test()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()


