#!/usr/bin/env python

"""
List zip file content.

Usage:
    python zip_files.py archive'
"""


import sys
import zipfile


def unpack(archive_file_name):
    zfile = zipfile.ZipFile(archive_file_name, 'r')
    info_objs = zfile.infolist()
    for idx, info_obj in enumerate(info_objs):
        print '%d. filename: %s (%d/%d)' % (idx + 1, info_obj.filename,
            info_obj.file_size, info_obj.compress_size, )
    zfile.close()

def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print __doc__
        sys.exit(1)
    archive_file_name = args[0]
    unpack(archive_file_name)


if __name__ == '__main__':
    main()

