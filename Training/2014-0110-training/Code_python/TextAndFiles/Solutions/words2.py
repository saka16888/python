#!/usr/bin/env python

"""Split each line in a file into words.  Count the words.

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
    """Count the occurance of each different word in a file.

    Return a dictionary containing the word counts.
    """
    infile = open(infilename, 'r')
    word_dict = {}
    for line in infile:
        words = split_words(line)
        for word in words:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
    infile.close()
    return word_dict

PAT1 = re.compile(r'\b(\w*)\b\W*')


def split_words(line):
    words = []
    pos1 = 0
    mo = PAT1.search(line, pos1)
    while mo is not None:
        word = mo.groups()[0]
        words.append(word)
        pos1 = mo.end()
        mo = PAT1.search(line, pos1)
    return words


def show_words(word_dict):
    count = 0
    for word, word_count in word_dict.iteritems():
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
