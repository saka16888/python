#!/usr/bin/env python

"""
Sample/template of implementation of a command line prompt.
"""

from cmd import Cmd


class Prompter(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = 'Hello: '

    def do_acmd(self, args):
        """This is command a.
        """
        print 'args:', args.split()

    def do_bcmd(self, args):
        """This is command b.
        """
        print 'args:', args.split()

    def do_ccmd(self, args):
        """This is command c.
        """
        print 'args:', args.split()

    def do_exit(self, args):
        """Exit from the command loop.
        """
        return True
    do_quit = do_exit


def test():
    prompter = Prompter()
    prompter.cmdloop('Welcome to our prompt.')


if __name__ == '__main__':
    test()
