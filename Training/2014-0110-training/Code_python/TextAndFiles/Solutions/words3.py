#!/usr/bin/env python

"""
Split each line in a file into words.  Count the words.  Use re.split().

Usage:
    python words.py [options] infile
Options:
    -h, --help      Display this help message.
Example:
    python words.py myfile.txt
"""


#
# Imports:
import sys
import getopt
import re


def count_words(infilename):
    """Count the words in a file.  Return a dictionary of words and counts.
    """
    infile = open(infilename, 'r')
    word_dict = {}
    for line in infile:
        if line.startswith('#'):
            continue
        words = split_words(line)
        for word in words:
            if word:
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1
    infile.close()
    return word_dict

PAT1 = re.compile(r'\W*')


def split_words(line):
    words = re.split(PAT1, line)
    return words


def show_words(word_dict):
    count = 0
    words = word_dict.keys()
    words.sort()
    for word in words:
        word_count = word_dict[word]
        print 'Word: "%s"  count: %d' % (word, word_count, )
        count += word_count
    print '=' * 40
    print 'Total words: %d' % (count, )


def test(infilename):
    word_dict = count_words(infilename)
    show_words(word_dict)


USAGE_TEXT = __doc__


def usage():
    print USAGE_TEXT
    sys.exit(1)


def main():
    args = sys.argv[1:]
    try:
        opts, args = getopt.getopt(args, 'h', ['help', ])
    except:
        usage()
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
    if len(args) != 1:
        usage()
    infilename = args[0]
    test(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
