#!/usr/bin/env python

"""
Sample code for creating and using builtin datatypes.
"""

import os
import glob
import pprint


def test_numbers():
    a1 = 123
    a2 = -456
    a3 = 0
    a4 = (a1 * a2) - a3
    a5 = 4.5
    a6 = -0.3
    a7 = a5 / a6
    a8 = 2
    a9 = float(a1) / a8
    print a1, a2, a3, a4, a5, a6, a7, a8, a9
    if a1 % 2 == 0:
        print "it's even"
    else:
        print "it's odd"


def test_lists_tuples():
    # --------------------------------------------
    # Creating tuples and lists.
    a1 = (11, 22, 33,)
    a2 = 'aaa', 'bbb', 'ccc', 'ddd',
    a3 = [44, 55, 66, 77]
    a4 = ['apple', 'banana', 'cumquat', 'date']
    a5 = [a1, a2]
    a6 = a3, a4
    a7 = [123, 'abc', 4.6, a6, a1, a3]
    a8 = list('abcd')
    print a1, a2, a3, a4, a5, a6, a7, a8
    # --------------------------------------------
    # Pretty-print a list.  See import above.
    pprint.pprint(a7)
    print 'len a7:', len(a7)
    # --------------------------------------------
    # Print the items in a list.
    for item in a4:
        print 'item:', item
    # --------------------------------------------
    # Append an item to a list.
    a4.append('elderberry')
    print 'a4:', a4
    # --------------------------------------------
    # Insert an item at a specific location in a list.
    a4.insert(0, 'fruit salad')
    print 'a4:', a4
    # --------------------------------------------
    # Add (concatonate) two lists together, producing a new list.
    #   Old lists are not modified.
    a8 = a3 + a4
    print 'a8:', a8
    # --------------------------------------------
    # Add the items of one list to another.  We could also use
    # mylist.extend(x).
    a8 += ['watermelon', 'cantaloupe', 'crenshaw', 'honeydew']
    print 'a8:', a8
    # --------------------------------------------
    # Cannot add tuple or list or list plus tuple.
    #a9 = a1 + a3
    # But we can extend a list with the (items in a) tuple.
    a3.extend(a1)
    print 'a3:', a3
    # --------------------------------------------
    # Indexing
    print 'a3[1]:', a3[1]
    # --------------------------------------------
    # Slicing
    print 'a3[1:3]:', a3[1:3]
    print 'a3[1:]:', a3[1:]
    print 'a3[:4]:', a3[:4]
    print 'a3[1:-1]:', a3[1:-1]
    print '1. a3.pop():', a3.pop()
    print '2. a3.pop():', a3.pop()
    print '1. a3:', a3
    # --------------------------------------------
    # Deleting an item from a list.
    del a3[1]
    print '2. a3:', a3
    x = a3
    # --------------------------------------------
    # Calling a function to modify a container object.
    append_item(a3, 99)
    print 'x:', x, 'a3:', a3
    print_list_of_list_of_ints()


#
# Teaching point: A function that modifies a mutable object changes
#     the object passed in from the calling code.
def append_item(collection, item):
    collection.append(item)


ListOfListOfInts = [
    [11, 22, 33, ],
    [44, 55, ],
    [66, 77, 88, 99, ],
]


def print_list_of_list_of_ints():
    for row in ListOfListOfInts:
        print 'length:', len(row)
        for item in row:
            print 'item:', item


def test_string():
    # --------------------------------------------
    a1 = ""
    a2 = "here's johnny"
    a3 = 'say "hi" to the folks'
    a4 = 'that\'s joe\'s way of saying "goodbye"'
    a5 = """line one
line two
line three
"""
    print a1
    print a2
    print a3
    print a4
    print a5
    # --------------------------------------------
    lines = []
    lines.append('a peanut butter sandwich')
    lines.append('a cheese sandwich')
    lines.append('a tomato sandwich')
    lines.append('a baloney sandwich')
    content = ' and '.join(lines)
    print 'content:', content
    # --------------------------------------------
    name = 'dave'
    print 'my name is %s and my name has %d letters' % (name, len(name), )
    # --------------------------------------------
    a6 = '    parsley and coriander and tarragon    '
    a7 = a6.strip()
    print 'a7:', a7
    a7 = a6.rstrip()
    print 'a7:', a7
    a7 = a6.lstrip()
    print 'a7:', a7
    print 'the position of coriander:', a6.find('coriander')
    # --------------------------------------------
    # Teaching point: Test for not found can *not* test for False.
    if a6.find('oregano') < 0:
        print 'we do not have oregano'
    else:
        print 'we have oregano'
    a8 = a6.replace('coriander', 'oregano')
    print 'a8:', a8
    # --------------------------------------------
    a9 = 'thyme'
    print '"%s"' % a9.ljust(10)
    print '"%s"' % a9.rjust(10)
    print 'words:', a6.split()
    print 'upper:', a8.upper()
    print 'lower:', a8.lower()
    # --------------------------------------------
    a10 = ['abc', 'def', 'ghi', ]
    print 'join:', '++'.join(a10)
    # --------------------------------------------
    # Count the number of "words" in a string.
    a11 = 'my garden has tomatoes and peppers and green beans'
    print count_words_in_string(a11)
    # --------------------------------------------
    # Do some formatting of strings in columns.
    format_to_screen()


StringData = """\
Alice Appleby:501-511-5101:1.5:bird watching
Bill Barnaby:501-511-5102:4009.2:gardening
Charlie Carbunkle:501-5103:54.251:hiking and bicycling
"""


def format_to_screen():
    print 'Name                Phone            Level Hobby'
    print '====                =====            ===== ====='
    for line in StringData.splitlines():
        s1 = format_line(line)
        print s1


def format_line(line):
    fields = line.split(':')
    if len(fields) == 4:
        name = fields[0].ljust(20)
        phone = fields[1].ljust(12)
        level = fields[2].rjust(10)
        hobby = fields[3].ljust(30)
        s1 = '%s%s%s %s' % (name, phone, level, hobby, )
    else:
        s1 = 'bad string'
    return s1


def count_words_in_string(str1):
    words = str1.split()
    count = len(words)
    return count, words


def test_dictionary():
    a1 = {}
    a2 = {
        'name': 'dave',
        'hobbies': ['birding', 'photography', ],
        'location': 'Sacramento',
    }
    print a1
    print a2
    # --------------------------------------------
    # Insert an item in a dictionary.
    a2['attitude'] = 'pretty good'
    print a2
    # --------------------------------------------
    # Print list of keys, values, and items/pairs in a dictionary.
    # Note that we can use a for: statement to iterate over these lists.
    print a2.keys()
    print a2.values()
    print a2.items()
    # --------------------------------------------
    # Test for the existence of a key in a dictionary.
    print "'location' in a2:", 'location' in a2
    print "'xxlocation' in a2:", 'xxlocation' in a2
    # --------------------------------------------
    # Use a dictionary to keep a count of different words in a string.
    word_dict = word_count(WordString)
    show_word_counts(word_dict)


WordString = 'the big dog has a big bark'


def word_count(word_str):
    word_list = word_str.split()
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict


def show_word_counts(word_dict):
    for word, count in word_dict.items():
        print 'word: "%s"  count: %d' % (word.ljust(12), count, )


def test_file():
    # --------------------------------------------
    # Open a text file for reading, then read the entire file at once.
    infile = open('small_file.txt', 'r')
    content = infile.read()
    infile.close()
    # --------------------------------------------
    # Split the content of the file into lines.
    lines = content.splitlines()
    for line in lines:
        print 'line:', line
    # --------------------------------------------
    # Iterate over the lines in a file.
    infile = open('small_file.txt', 'r')
    lineno = 1
    for line in infile:
        print '%d. line: "%s"' % (lineno, line.rstrip(), )
        lineno += 1
    print 'number of lines:', lineno
    infile.close()
    # --------------------------------------------
    # Iterate over the lines in a file.  Count the number of words.
    infile = open('small_file.txt', 'r')
    count = 0
    for line in infile:
        print 'line:', line.rstrip()
        words = line.split()
        count += len(words)
    print 'count:', count
    infile.close()
    # --------------------------------------------
    # Open a file for writing.  Write a few lines to the file.
    outfile = open('tmp01.dat', 'w')
    outfile.write('something\n')
    outfile.write('or\n')
    outfile.write('other\n')
    outfile.close()
    outfile = open('tmp01.dat', 'a')
    outfile.write('more stuff\n')
    outfile.close()
    # --------------------------------------------
    # Get a list of the names of files that satisfy a pattern.
    # See import above.
    print glob.glob('*.py')
    print 'path' + os.sep + 'to' + os.sep + 'file'


def hr(msg):
    print '-' * 60
    print msg
    print '-' * len(msg)


#
# Run all the tests.
def test():
    hr('Numbers:')
    test_numbers()
    hr('Lists and tuples:')
    test_lists_tuples()
    hr('Strings:')
    test_string()
    hr('Dictionaries:')
    test_dictionary()
    hr('Files:')
    test_file()


if __name__ == '__main__':
    test()
