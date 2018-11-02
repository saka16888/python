#!/usr/bin/env python

"""
Sample code for Python statements.
"""

import sys
from xml.dom import minidom                 # [1]
from xml.dom.minidom import parse           # [2]
from xml.dom import minidom as md           # [3]
import types


def import_statement():
    hr('import statement')
    print 'sys.path:'
    for path in sys.path:
        print '   ', path
    # Dereference into the minidom module.  See [1] above.
    doc = minidom.parse('plant_catalog_01.xml')
    # Access an attribute of the minidom module directly.  See [2] above.
    doc = parse('plant_catalog_01.xml')
    # Use the renamed minidom module.  See [3] above.
    doc = md.parse('plant_catalog_01.xml')
    print doc


def assignment_statement():
    hr('assignment statement')
    # -----------------------------------------------------
    a1 = (111, 222, 333)
    b1, b2, b3 = a1
    print b1, b2, b3
    # -----------------------------------------------------
    # Assign a value to a position in a list.
    a1 = [11, 22, 33, 44]
    print a1
    a1[1] = 'aa'
    a1[2] = '4.5'
    print a1
    # -----------------------------------------------------
    # Associate a value with a key in a dictionary.
    a2 = {}
    a2['name'] = 'tomato'
    a2['size'] = 25
    # -----------------------------------------------------
    # Augmented assignment
    c1 = 23
    print '1. c1:', c1
    c1 += 1
    print '2. c1:', c1
    c1 *= 3
    print '3. c1:', c1


def print_statement():
    hr('print statement')
    print 'aaa', 'bbb', 'ccc',
    print 'ddd'
    sys.stdout.write('writing to stdout\n')
    sys.stdout.write('notice the newline character\n')


def do_add():
    pass


def do_del():
    pass


def do_show():
    pass


def do_error():
    pass


ARRAY_1 = [1, 2, 3, 4, 5, ]
ARRAY_2 = [11, 22, 33, 44, 55, ]


def for_statement():
    hr('for statement')
    # -----------------------------------------------------
    # Print out the items in a list/collection.
    a1 = ['aaa', 'bbb', 'ccc', 'ddd', ]
    for item in a1:
        print 'item: %s' % (item, )
    # -----------------------------------------------------
    # Exit from the for: loop when we find a 'bbb'.
    for item in a1:
        if item == 'bbb':
            break
        print 'item: %s' % (item, )
    print 'finished loop'
    # -----------------------------------------------------
    # Skip the item 'bbb'.
    for item in a1:
        if item == 'bbb':
            continue
        print 'item: %s' % (item, )
    # -----------------------------------------------------
    # Use enumerate() to also print an index.
    for idx, item in enumerate(a1):
        print '%d. item: %s' % (idx, item, )
    # -----------------------------------------------------
    # Process all the items in a dictionary.
    person = {
        'name': 'dave',
        'hobbies': ['birding', 'photography', ],
        'location': 'Sacramento',
    }
    for key, value in person.items():
        print 'key: %s  value: %s' % (key.ljust(12), value, )
    # -----------------------------------------------------
    dict1 = {
        'aa': 111,
        'bb': 222,
        'cc': 333,
    }
    collection1 = [123, 'aaa', [11, 22], dict1, 1.23, ]
    for item in collection1:
        if isinstance(item, types.StringType):
            print '"%s" is an string' % item
        elif isinstance(item, types.IntType):
            print '%s is an integer' % item
        elif isinstance(item, types.ListType):
            print '%s is a list' % item
        elif isinstance(item, types.DictType):
            print '%s is a dictionary' % item
        else:
            print '%s is none of the above' % item
    # -----------------------------------------------------
    # Use enumerate() and a for: statement to update one list from another.
    print '1. ARRAY_1: %s' % (ARRAY_1, )
    print '1. ARRAY_2: %s' % (ARRAY_2, )
    for idx, item in enumerate(ARRAY_1):
        ARRAY_2[idx] += item
    print '2. ARRAY_1: %s' % (ARRAY_1, )
    print '2. ARRAY_2: %s' % (ARRAY_2, )


def while_statement():
    hr('while statement')
    # -----------------------------------------------------
    count = 0
    max = 5
    while count < max:
        print 'line %d' % count
        count += 1
    # -----------------------------------------------------
    items = ['abc', 'def', 'ghi', ]
    while len(items) > 0:
        print items.pop()
    # -----------------------------------------------------
    # Teaching point only: Better to use for: statement to read lines of file.
    infile = open('small_file.txt')
    line = infile.readline()
    while line:
        print 'the line:', line
        line = infile.readline()
    infile.close()
    # -----------------------------------------------------
    # Use while: statement to update one list from another.
    print '1. ARRAY_1: %s' % (ARRAY_1, )
    print '1. ARRAY_2: %s' % (ARRAY_2, )
    idx = 0
    while idx < len(ARRAY_1):
        ARRAY_2[idx] += ARRAY_1[idx]
        idx += 1
    print '2. ARRAY_1: %s' % (ARRAY_1, )
    print '2. ARRAY_2: %s' % (ARRAY_2, )


def break_statement():
    hr('break statement')
    # -----------------------------------------------------
    # Exit from a while: statement with break statement.
    infile = open('small_file.txt')
    line = infile.readline()
    while line:
        if line.startswith('third'):
            break
        print 'the line:', line
        line = infile.readline()
    infile.close()
    # -----------------------------------------------------
    # Exit from a for: statement with break statement.
    infile = open('small_file.txt')
    for line in infile:
        if line.startswith('third'):
            break
        print 'the line:', line
    infile.close()


def continue_statement():
    hr('continue statement')
    # -----------------------------------------------------
    # Skip items that are even with continue statement.
    for item in ARRAY_2:
        if item % 2 == 0:
            continue
        print 'an odd item: %d' % (item, )


def if_elif_else_statement():
    hr('if:elif:else statement')
    a1 = 4
    print a1 > 3
    print 2 < a1 and a1 < 5
    # See note on chaining at:
    #     http://docs.python.org/ref/comparisons.html#comparisons
    print 2 < a1 < 5
    if a1 > 2:
        print "it's bigger than 2"
    cmd = 'show'
    # -----------------------------------------------------
    # Python's "switch" statement version 1.
    if cmd == 'add':
        do_add()
    elif cmd == 'del':
        do_del()
    elif cmd == 'show':
        do_show()
    else:
        print 'bad command:', cmd
    # -----------------------------------------------------
    # Python's "switch" statement version 2.
    cmd_map = {
        'add': do_add,
        'del': do_del,
        'show': do_show,
    }
    f = cmd_map.get(cmd, do_error)
    f()


class MyException(Exception):
    pass


def raise_my_exception():
    print 'before myexception 2'
    raise_my_exception_1()
    print 'after myexception 2'


def raise_my_exception_1():
    print 'before myexception 3'
    # Teaching point only.  Usually, only one argument, a message.
    raise MyException('arg #1', 'arg #2', 'arg #3')
    print 'after myexception 3'


def try_statement():
    hr('try statement')
    try:
        infile = open('xxyyzz.txt', 'r')
        print "file %s is open" % (infile, )
    except IOError, exp:
        print 'file not there'
        print '[[[', exp, ']]]'
        print 'exp.message:', exp.message
        print 'exp.args:', exp.args
    try:
        print 'before myexception 1'
        raise_my_exception()
        print 'after myexception 1'
    except MyException, excp:
        print 'MyException -- excp.args:', excp.args


class Context01(object):

    def __enter__(self):
        print 'in __enter__'
        return 'some value or other'

    def __exit__(self, exc_type, exc_value, traceback):
        print 'in __exit__'


def with_statement():
    hr('with statement')
    with Context01():
        print 'in body'
    with Context01() as a_value:
        print 'in body'
        print 'a_value: "%s"' % (a_value, )


def hr(msg):
    print '-' * 40
    print msg
    print '-' * 40


def test():
    assignment_statement()
    print_statement()
    if_elif_else_statement()
    for_statement()
    while_statement()
    break_statement()
    continue_statement()
    try_statement()
    import_statement()
    with_statement()


test()
