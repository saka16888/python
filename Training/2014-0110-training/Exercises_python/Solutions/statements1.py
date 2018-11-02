#!/usr/bin/env python

import traceback


#
# assignment statement
#
def test_assignment():
    value1 = 'abc'
    print 'value1:', value1
    value2 = 23
    print 'value2:', value2
    value2 += 1
    print 'value2:', value2
    value2 -= 1
    print 'value2:', value2
    items = 23, 45, 67
    a, b, c = items
    print 'a:', a, 'b:', b, 'c:', c
    value3 = {}
    value3['fruit'] = 'tangerine'
    print 'value3:', value3


#
# for statement
#
def test_for():
    data1 = [11, 22, 33, 44]
    data2 = range(4)
    print 'data1:', data1
    print 'data2:', data2
    print '-' * 20
    for item in data1:
        print 'item:', item
    print '-' * 20
    for idx, item in enumerate(data1):
        print 'idx:', idx, ' item:', item
    print '-' * 20
    for idx, item in enumerate(data1):
        if idx % 2 == 0:
            print 'idx:', idx, ' item:', item
    print '-' * 20
    for idx, item in enumerate(data1):
        if idx % 2 != 0:
            continue
        print 'idx:', idx, ' item:', item
    print '-' * 20
    print 'data1       :', data1
    print 'data2 before:', data2
    for idx, item in enumerate(data1):
        data2[idx] = data1[idx] + data2[idx]
    print 'data2 after :', data2
    data2 = [x * 2 for x in data1]
    print 'data2:', data2
    data3 = [x * 3 for x in data1 if x % 2 == 0]
    print 'data3:', data3
    data4 = "aaa bbb  ,   ccc ddd  , eee fff ggg"
    data5 = [field.strip() for field in data4.split(',')]
    print 'data4: "%s"' % data4
    print 'data5:', data5
    value1 = 'not found'
    for item in data1:
        if item > 100:
            value1 = item
            break
    print 'value1:', value1
    for item in data1:
        if item > 100:
            value1 = item
            break
    else:
        value1 = 'not found'
    print 'value1:', value1
    for item in data1:
        if item > 30:
            value1 = item
            break
    else:
        value1 = 'not found'
    print 'value1:', value1


#
# if statement
#
def test_if():
    list1 = ['apple', 'banana', 'cherry', 'date', ]
    for item in list1:
        if item == 'apple':
            print "it's an apple"
        elif item == 'banana':
            print "it's a banana"
        elif item == 'cherry':
            print "it's a cherry"
        else:
            print "it's an other --", item
    v1 = 3
    v2 = 5
    v3 = 7
    if not (v1 < v2 and v2 < v3) or v1 != v2:
        print 'yes'
    else:
        print 'no'
    list2 = range(10)
    value1 = 5
    value2 = 20
    if value1 in list2:
        print "it's in -- %d" % value1
    if value2 not in list2:
        print "it's not -- %d" % value2
    dict1 = {'watermelon': 4}
    key1 = 'watermelon'
    if key1 in dict1 and dict1[key1] == 4:
        print "it's good"
    key2 = 'cantaloupe'
    if key2 in dict1 and dict1[key2] == 4:
        print "it's bad"


#
# while statement
#
def test_while(word_length):
    words = ['a', 'bb', 'ccc', 'dddd', ]
    idx = 0
    word = None
    while idx < len(words):
        if len(words[idx]) == word_length:
            word = words[idx]
            break
        idx += 1
    print 'word: "%s"' % word
    print '-' * 20
    word_length += 20
    while idx < len(words):
        if len(words[idx]) == word_length:
            word = words[idx]
            break
        idx += 1
    else:
        word = None
    print 'word: "%s"' % word
    print '-' * 20
    items = range(10, 14)
    while items:
        item = items.pop()
        print 'popped item:', item
    return word


def search_positions(pat, target):
    pos = 0
    while True:
        pos = target.find(pat, pos)
        if pos < 0:
            break
        print 'search pos:', pos
        pos += 1


def generate_positions(pat, target):
    pos = 0
    while True:
        pos = target.find(pat, pos)
        if pos < 0:
            break
        yield pos
        pos += 1


def apply_at_positions(pat, target, func):
    pos = 0
    while True:
        pos = target.find(pat, pos)
        if pos < 0:
            break
        func(pos, target[pos:pos+len(pat)])
        pos += 1


def func1(pos, str_val):
    print 'apply at pos: %d  "%s"' % (pos, str_val.upper(), )


#
# try/except and raise statements
#

class SpecialException(Exception):
    pass


def fn1():
    print '(fn1) before'
    fn2()
    print '(fn1) after'


def fn2():
    print '(fn2) before'
    fn3()
    print '(fn2) after'


def fn3():
    print 'before raising exception'
    raise SpecialException('this is the end; my only friend the end')
    print 'after raising exception'


def test_try_except():
    #fn1()
    try:
        fn1()
    except SpecialException as exp:
        print 'exp:', exp


#
# with statement
#
class Wrapper(object):
    def __enter__(self):
        print 'entering'
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type is None:
            print 'exiting normally'
        elif exc_type is ZeroDivisionError:
            print 'caught exception "{}" and continuing'.format(exc_value)
            print '-' * 40
            traceback.print_tb(exc_traceback)
            print '-' * 40
            # Tell Python to suppress the exception (continue execution).
            return True
        else:
            print 'caught exception "{}" and aborting'.format(exc_value)

    def printer(self, msg):
        print '== {} =='.format(msg)


def test_with():
    with Wrapper() as wrap:
        wrap.printer('1. hello')
        wrap.printer('1. goodbye')
    with Wrapper() as wrap:
        wrap.printer('2. hello')
        # an error
        1 / 0
        wrap.printer('2. goodbye')
    with Wrapper() as wrap:
        wrap.printer('3. hello')
        # another error.  Uncomment the next line to test exception
        # handling in the Wrapper class.
        #hr()
        wrap.printer('3. goodbye')


def hr(label, length=60):
    print '-' * length
    print '    %s' % label
    print '-' * length


def test():
    hr('assignment')
    test_assignment()
    hr('for')
    test_for()
    hr('while')
    print test_while(3)
    print '-' * 20
    search_positions('xxx', 'aaaxxxbbbxxxcccxxxdddxxxeee')
    print '-' * 20
    generator1 = generate_positions('xxx', 'aaaxxxbbbxxxcccxxxdddxxxeee')
    for pos in generator1:
        print 'generate pos:', pos
    print '-' * 20
    apply_at_positions('xxx', 'aaaxxxbbbxxxcccxxxdddxxxeee', func1)
    hr('if')
    test_if()
    hr('try_except')
    test_try_except()
    hr('with')
    test_with()


if __name__ == '__main__':
    test()
