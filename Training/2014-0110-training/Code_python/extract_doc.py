#!/usr/bin/env python

"""
Use the pydoc module to extract information from the module doc string.

Usage:
    python extract_doc.py [options] file1 file2 ...
Options:
    -h, --help		Print this usage information.
    -v, --verbose   Print out extra info
    -r, --rest		Generate reST/reStructuredText (default: plain text)
    -t, --title=    Document title
    -o, --outfile=  Output file name (default: sys.stdout)
"""


#
# Imports:
import sys
import os
import getopt
import pydoc


#
# Functions for internal use:
def extract(filenames, verbose, rest, title, outfile):
    """Modify or replace this function for your own needs.
    """
    if rest:
        titlelen = len(title)
        print >> outfile, '=' * titlelen
        print >> outfile, title
        print >> outfile, '=' * titlelen
        module_list = []
    for filename in filenames:
        if verbose:
            print 'adding file: %s' % (filename, )
        modname = os.path.splitext(os.path.split(filename)[1])[0]
        modname = os.path.split(filename)[1]
        synopsis = pydoc.synopsis(modname)
        if rest:
            module_list.append(modname)
            print >> outfile
            s1 = '- `%s <%s>`_ (`%s.html <%s.html>`_, ' + \
                '`%s.pdf <%s.pdf>`_) -- %s' % (
                modname, modname,
                modname, modname,
                modname, modname,
                synopsis, )
            print >> outfile, s1
        else:
            print >> outfile, '--'
            print >> outfile, '%s' % modname
            print >> outfile, synopsis
    print
##     for name in module_list:
##         print >> outfile, '_`%s.py.html`: %s.py.html' % (name, name, )
##         print
##         print >> outfile, '_`%s.py.pdf`: %s.py.pdf' % (name, name, )
##         print


USAGE_TEXT = __doc__


def usage():
    print USAGE_TEXT
    sys.exit(1)


def main():
    args = sys.argv[1:]
    try:
        opts, args = getopt.getopt(args, 'hvrt:o:', [
            'help',
            'verbose', 'rest', 'title=',
            'outfile=',
        ])
    except:
        usage()
    verbose = False
    rest = False
    title = 'Directory listing'
    outfilename = None
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt in ('-v', '--verbose'):
            verbose = True
        elif opt in ('-r', '--rest'):
            rest = True
        elif opt in ('-t', '--title'):
            title = val
        elif opt in ('-o', '--outfile'):
            outfilename = val
    if len(args) < 1:
        usage()
    filenames = args
    if outfilename is None:
        outfile = sys.stdout
    else:
        outfile = open(outfilename, 'w')
    extract(filenames, verbose, rest, title, outfile)
    if outfilename is not None:
        outfile.close()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
