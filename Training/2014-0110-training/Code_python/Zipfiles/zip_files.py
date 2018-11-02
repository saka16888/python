#!/usr/bin/env python

"""
Create zip file from list of file names.

Usage:
    python zip_files.py archive file1 file2 ...'
"""


import sys
import zipfile


def pack(archive_file_name, file_names):
    out_file = open(archive_file_name, 'w', zipfile.ZIP_DEFLATED)
    zfile = zipfile.ZipFile(out_file, 'w')
    for file_name in file_names:
        print 'Adding %s' % (file_name, )
        zfile.write(file_name, file_name, zipfile.ZIP_DEFLATED)
    zfile.close()
    out_file.close()

def main():
    args = sys.argv[1:]
    if len(args) < 2:
        print __doc__
        sys.exit(1)
    archive_file_name = args[0]
    file_names = args[1:]
    pack(archive_file_name, file_names)

if __name__ == '__main__':
    main()

