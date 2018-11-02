#!/usr/bin/env python

"""
A command line prompt for regular expression operations.

Also demonstrates delegation of operations from one class to another.

Usage:
    python re_scan.py [options] command pat repl file_pat
Options:
    -h, --help      Display this help message.
Commands:
    scan         Scan for pattern.  args: scan pat file
    repl         Scan and replace.  args: repl pat replacement file
    extract      Extract and show matches.  args: extract pat file
    command      Start command line loop.  args: command file
Example:
    python re_scan.py scan albert somefile.txt
    python re_scan.py repl albert bertrand somefile.txt
    python re_scan.py scan albert somefile.txt
    python re_scan.py command somefile.txt
"""


#
# Imports:
import sys
import getopt
import re
import glob
import cmd


#
# Global variables and constants:

PAT1 = re.compile(r'^class')


#
# Functions for external use, factories, etc:



#
# Classes:



class RegExprUtils(object):
    def __init__(self, file_pat):
        self.file_pat = file_pat
        self.file_names = glob.glob(file_pat)

    def get_file_names(self):
        return self.file_names

    def scan(self, pat):
        """Scan files for lines matching regexp.  Print matching lines.
        """
        re_pat = re.compile(pat)
        for infilename in self.file_names:
            infile = open(infilename, 'r')
            for line in infile:
                line = line.rstrip()
                mo = re_pat.search(line)
                if mo is not None:
                    print '%s:%s' % (infilename, line, )

    def replace(self, pat, repl):
        """Scan files for match and replace.
        """
        re_pat = re.compile(pat)
        for infilename in self.file_names:
            infile = open(infilename, 'r')
            for line in infile:
                line = line.rstrip()
                line1 = re_pat.sub(repl, line)
                if line1 != line:
                    print 'Repl: %s' % (line1, )
                
    def extract(self, pat):
        """Scan files for match and extract group.  Show items in group.
        """
        re_pat = re.compile(pat)
        for infilename in self.file_names:
            infile = open(infilename, 'r')
            for lineno, line in enumerate(infile):
                line = line.rstrip()
                mo = re_pat.search(line)
                if mo is not None:
                    groups = mo.groups()
                    print 'File: %s  LnNo: %d  Line: %s' % (
                        infilename, lineno, line, )
                    for item in groups:
                        print '    Match: "%s"' % (item, )
                    

class Prompter(cmd.Cmd):
    def __init__(self, file_pat):
        cmd.Cmd.__init__(self)
        self.prompt = 'RegExpr: '
        self.regexprutils = RegExprUtils(file_pat)

    def do_files(self, args):
        """Print out the names of files to be searched.
        """
        file_names = self.regexprutils.get_file_names()
        print 'File names:'
        for name in file_names:
            print '    %s' % (name, )

    def do_scan(self, args):
        """Scan/search the files in file_pat.
        """
        args = args.split()
        if len(args) != 1:
            print 'usage: scan pat'
            return
        pat = args[0]
        print 'pat: "%s"' % pat
        self.regexprutils.scan(pat)

    def do_repl(self, args):
        """Search and replace in files (but do not replace on disk).
        """
        args = args.split()
        if len(args) != 2:
            print 'usage: scan pat'
            return
        pat = args[0]
        repl = args[1]
        self.regexprutils.replace(pat, repl)

    def do_extract(self, args):
        """Extract and show matching groups.
        """
        args = args.split()
        if len(args) != 1:
            print 'usage: scan pat'
            return
        pat = args[0]
        self.regexprutils.extract(pat)


    def do_exit(self, args):
        """Exit from the command loop.
        """
        sys.exit(1)
    do_quit = do_exit

    do_h = cmd.Cmd.do_help

    def emptyline(self):
        pass



#
# Functions for internal use:




USAGE_TEXT = __doc__

def usage():
    print USAGE_TEXT
    sys.exit(1)


def main():
    args = sys.argv[1:]
    try:
        opts, args = getopt.getopt(args, 'hva:', ['help',
             ])
    except:
        usage()
    verbose = False
    avalue = None
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
    if len(args) < 1:
        usage()
    print 'args:', args
    command = args[0]
    if command == 'scan':
        if len(args) != 3:
            usage()
        pat = args[1]
        file_pat = args[2]
        scanner = RegExprUtils(file_pat)
        scanner.scan(pat)
    elif command == 'repl':
        if len(args) != 4:
            usage()
        pat = args[1]
        repl = args[2]
        file_pat = args[3]
        scanner = RegExprUtils(file_pat)
        scanner.replace(pat, repl)
    elif command == 'extract':
        if len(args) != 3:
            usage()
        pat = args[1]
        file_pat = args[2]
        scanner = RegExprUtils(file_pat)
        scanner.extract(pat)
    elif command == 'command':
        if len(args) != 2:
            usage()
        file_pat = args[1]
        prompter = Prompter(file_pat)
        prompter.cmdloop()
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()


