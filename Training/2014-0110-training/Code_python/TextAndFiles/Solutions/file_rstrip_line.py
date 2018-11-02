#!/usr/bin/env python


"""
Wrapper class for file data type that filters and rstrip's lines.
"""

import sys


class FileLineStrip(object):
    """Wrap the file class/type and add newline stripping.
    """
    def __init__(self, *args, **kwargs):
        self.infile = open(*args, **kwargs)

    def readline(self):
        line = self.infile.readline()
        line = self.filter(line)
        return line

    def next(self):
        line = self.infile.next()
        line = self.filter(line)
        return line

    def close(self):
        self.infile.close()

    def __iter__(self):
        return self

    def filter(self, line):
        line = line.rstrip('\n')
        return line


class SubclassFileLineStrip(file):
    """Subclass the file class/type and add newline stripping.
    """
    def next(self):
        line = file.next(self)
        line = self.filter(line)
        return line

    def readline(self):
        line = file.readline(self)
        line = self.filter(line)
        return line

    def filter(self, line):
        line = line.rstrip('\n')
        return line


class SubclassFileLineFilter(file):
    """Subclass the file class/type and add newline stripping.
    """
    def __init__(self, filename, mode='r', buffering=1, filterfunc=None):
        file.__init__(self, filename, mode, buffering)
        if filterfunc is None:
            raise RuntimeError, 'Must supply arg fulterfunc (filter function).'
        self.filterfunc = filterfunc

    def set_filterfunc(self, filterfunc):
        self.filterfunc = filterfunc

    def next(self):
        line = file.next(self)
        line = self.filterfunc(line)
        return line

    def readline(self):
        line = file.readline(self)
        line = self.filterfunc(line)
        return line

    def filter(self, line):
        line = line.rstrip('\n')
        return line


def filter1(line):
    line = '##%s' % line.rstrip('\n')
    return line


def test():
    args = sys.argv[1:]
    if len(args) != 1:
        print 'usage: file_rstrip_line.py infilename'
        sys.exit(1)
    infilename = args[0]
    infile = FileLineStrip(infilename)
    for line in infile:
        print '1. line:', line
    infile.close()
    print '-' * 40
    infile = FileLineStrip(infilename)
    line = infile.readline()
    while line:
        print '2. line:', line
        line = infile.readline()
    infile.close()
    print '-' * 40
    infile = SubclassFileLineStrip(infilename)
    for line in infile:
        print '3. line:', line
    infile.close()
    print '-' * 40
    infile = SubclassFileLineFilter(infilename, filterfunc=filter1)
    #infile = SubclassFileLineFilter(infilename)
    for line in infile:
        print '4. line:', line
    infile.close()

if __name__ == '__main__':
    test()

