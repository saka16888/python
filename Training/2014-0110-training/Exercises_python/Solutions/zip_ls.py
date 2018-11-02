#!/usr/bin/env python

"""
Synopsis:
    Print formatted listing of Zip file.
Usage:
    python zip-ls.py [options] <zip_file_name>
Options:
    -h, --help      Display this help message.
    -s, --sort      Sort files by x, where x is one of:
                        file_name     or fn (default)
                        date_time     or dt
                        file_size     or fs
                        compress_size or cs
    -c, --columns   Columns to display.  Values:
                        s   Short; file names only.
                        m   Medium (default)
                        l   Long
                        v   Verbose
    -r, --reverse   Reverse sort
    -t, --totals    Print column totals.
    --no-totals     Do not print column totals.  (override .zip-lsrc)
Examples:
    python zip-ls.py stuff.zip
    python zip-ls.py -s file_name stuff.zip
    python zip-ls.py --sort=date_time --reverse stuff.zip
    python zip-ls.py -s compress_size -c m stuff.zip

zip-ls reads default options from ${HOME}/.zip-lsrc.  Example
of .zip-lsrc:

    [general]
    sort: file_name
    columns: v
    reverse: 0
    totals: 1
Hints:
    - zipfile module in the Python standard library
    - ConfigParser module in the Python standard library
"""


import sys
import os
import getopt
import zipfile
import ConfigParser


class Accumulator:
    """Simple class used to accumulate results: count, total file size,
    and total compressed size.
    """
    def __init__(self):
        """ Initialize counts and totals.
        """
        self.count = 0
        self.file_size = 0
        self.compress_size = 0


def listArchive(outstream, sortFlag, columns, reverse, totals, zipFileName):
    wrt = outstream.write
    path, ext = os.path.splitext(zipFileName)
    if not ext:
        zipFileName = '%s.zip' % path
##    ipshell = IPShellEmbed()
##    ipshell('Starting listArchive()\nCtrl-D to exit.')
    zf = zipfile.ZipFile(zipFileName, 'r')
    zl = zf.infolist()
##     IPython.embed()
##     from ipdb import set_trace; set_trace()
    if sortFlag in ('file_name', 'fn'):
        zl.sort(sortfunc_name)
    elif sortFlag in ('date_time', 'dt'):
        zl.sort(sortfunc_date_time)
    elif sortFlag in ('file_size', 'fs'):
        zl.sort(sortfunc_file_size)
    elif sortFlag in ('compress_size', 'cs'):
        zl.sort(sortfunc_compress_size)
    else:
        usage()
    if reverse:
        zl.reverse()
    accumulator = Accumulator()
    for item in zl:
        line = formatLine(item, columns, accumulator)
        wrt(line)
    if totals:
        if columns == 's':
            wrt('----\n')
        elif columns == 'm':
            wrt('--------                    ----\n')
        elif columns == 'l':
            wrt('-------- -------- ----                    ----\n')
        elif columns == 'v':
            wrt('-------- -------- ----                              ----\n')
        line = formatTotalLine(columns, accumulator)
        wrt(line)


def formatLine(item, columns, accumulator):
    if columns == 's':
        line = '%s\n' % item.filename
    elif columns == 'm':
        file_size = str(item.file_size)
        date = formatDate(item.date_time)
        line = '%s  %s  %s\n' % \
            (file_size.rjust(8), date.rjust(16), item.filename)
    elif columns == 'l':
        file_size = str(item.file_size)
        compress_size = str(item.compress_size)
        date = formatDate(item.date_time)
        if item.file_size <= 0:
            ratio = 0
        else:
            ratio = (float(item.file_size) - float(item.compress_size)) / \
                float(item.file_size)
        ratioStr = '%2.0f' % (ratio * 100)
        line = '%s %s  %s%%  %s  %s\n' % (
            file_size.rjust(8),
            compress_size.rjust(8),
            ratioStr,
            date.rjust(16),
            item.filename
        )
    elif columns == 'v':
        file_size = str(item.file_size)
        compress_size = str(item.compress_size)
        date = formatDate(item.date_time)
        crc = '%08x' % item.CRC
        if item.file_size <= 0:
            ratio = 0
        else:
            ratio = (float(item.file_size) - float(item.compress_size)) / \
                float(item.file_size)
        ratioStr = '%2.0f' % (ratio * 100)
        # ratioStr = ratioStr[2:]
        line = '%s %s  %s%%  %s  %s  %s\n' % (
            file_size.rjust(8),
            compress_size.rjust(8),
            ratioStr,
            date.rjust(16),
            crc,
            item.filename
        )
    else:
        usage()
    accumulator.count += 1
    accumulator.file_size += item.file_size
    accumulator.compress_size += item.compress_size
    return line


def formatDate(date_time):
    date = '%04d-%02d-%02d %02d:%02d' % (
        date_time[0], date_time[1],
        date_time[2], date_time[3],
        date_time[4])
    return date


def formatTotalLine(columns, accumulator):
    if columns == 's':
        if accumulator.file_size <= 0:
            ratio = 0
        else:
            ratio = ((float(accumulator.file_size) -
                     float(accumulator.compress_size)) /
                     float(accumulator.file_size))
        ratioStr = '%2.0f' % (ratio * 100)
        line = '%d files\n' % (accumulator.count,)
    elif columns == 'm':
        line = '%s                    %d files\n' % (
            str(accumulator.file_size).rjust(8),
            accumulator.count
        )
    elif columns == 'l':
        if accumulator.file_size <= 0:
            ratio = 0
        else:
            ratio = ((float(accumulator.file_size) -
                     float(accumulator.compress_size)) /
                     float(accumulator.file_size))
        ratioStr = '%2.0f' % (ratio * 100)
        line = '%s %s  %s%%                    %d files\n' % (
            str(accumulator.file_size).rjust(8),
            str(accumulator.compress_size).rjust(8),
            ratioStr,
            accumulator.count
        )
    elif columns == 'v':
        if accumulator.file_size <= 0:
            ratio = 0
        else:
            ratio = ((float(accumulator.file_size) -
                     float(accumulator.compress_size)) /
                     float(accumulator.file_size))
        ratioStr = '%2.0f' % (ratio * 100)
        line = '%s %s  %s%%                              %d files\n' % (
            str(accumulator.file_size).rjust(8),
            str(accumulator.compress_size).rjust(8),
            ratioStr,
            accumulator.count
        )
    return line


def sortfunc_name(item1, item2):
    if item1.filename < item2.filename:
        return -1
    elif item1.filename > item2.filename:
        return 1
    else:
        return 0


def sortfunc_date_time(item1, item2):
    if item1.date_time < item2.date_time:
        return -1
    elif item1.date_time > item2.date_time:
        return 1
    else:
        return 0


def sortfunc_file_size(item1, item2):
    if item1.file_size < item2.file_size:
        return -1
    elif item1.file_size > item2.file_size:
        return 1
    else:
        return 0


def sortfunc_compress_size(item1, item2):
    if item1.compress_size < item2.compress_size:
        return -1
    elif item1.compress_size > item2.compress_size:
        return 1
    else:
        return 0


def getDefaultOptions():
    """Get _default_ options from ${HOME}/.zip-lsrc using
    ConfigParser.ConfigParser().
    """
    sortFlag = 'file_name'
    columns = 'm'
    reverse = 0
    totals = 0
    home = os.getenv('HOME')
    if home:
        rcpath = '%s/.zip-lsrc' % home
        parser = ConfigParser.ConfigParser()
        parser.read(rcpath)
        if parser.has_section('general'):
            if parser.has_option('general', 'sort'):
                sortFlag = parser.get('general', 'sort')
            if parser.has_option('general', 'columns'):
                columns = parser.get('general', 'columns')
            if parser.has_option('general', 'reverse'):
                reverse = parser.get('general', 'reverse')
                if reverse in ('1', 'True'):
                    reverse = 1
                else:
                    reverse = 0
            if parser.has_option('general', 'totals'):
                totals = parser.get('general', 'totals')
                if totals in ('1', 'True'):
                    totals = 1
                else:
                    totals = 0
    return (sortFlag, columns, reverse, totals)


USAGE_TEXT = __doc__


def usage():
    print USAGE_TEXT
    sys.exit(-1)


def main():
    args = sys.argv[1:]
    try:
        opts, args = getopt.getopt(
            args, 'hs:c:rt',
            ['help', 'sort=', 'columns=', 'reverse', 'totals',
                'no-totals', ])
    except:
        usage()
    sortFlag, columns, reverse, totals = getDefaultOptions()
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt in ('-s', '--sort'):
            sortFlag = val
        elif opt in ('-c', '--columns'):
            columns = val
        elif opt in ('-r', '--reverse'):
            reverse = 1
        elif opt in ('-t', '--totals'):
            totals = 1
        elif opt in ('--no-totals', ):
            totals = 0
    if len(args) != 1:
        usage()
    listArchive(sys.stdout, sortFlag, columns, reverse, totals, args[0])


if __name__ == '__main__':
    main()
    #import pdb
    #pdb.run('main()')
