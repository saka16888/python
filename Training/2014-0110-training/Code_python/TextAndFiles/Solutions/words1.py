#!/usr/bin/env python

"""
Create dictionary of word occurances and counts.
"""


S1 = 'the big dog has a big bark'


def count(word_str):
    word_list = word_str.split()
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict


def show(word_dict):
    for word, count in word_dict.items():
        print 'word: "%s"  count: %d' % (word.ljust(12), count, )


def test():
    word_dict = count(S1)
    show(word_dict)


if __name__ == '__main__':
    test()
