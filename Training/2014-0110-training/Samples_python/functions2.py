#!/usr/bin/env python

"""
Sample code for definition of function arguments.
"""


#
# A function requiring no arguments and two return values.
def f1():
    print 'hello'
    return 4, 'a simple message'


#
# A function with 3 plain formal parameters.  It requires 3 actual arguments.
def f2(arg1, arg2, arg3):
    print 'f2 -- arg1:', arg1
    print 'f2 -- arg2:', arg2
    print 'f2 -- arg3:', arg3


#
# A function with two plain formal parameters and two optional
# formal parameters.
def f3(arg1, arg2, arg3='ccc', arg4='ddd'):
    print 'f3 -- arg1:', arg1
    print 'f3 -- arg2:', arg2
    print 'f3 -- arg3:', arg3
    print 'f3 -- arg4:', arg4


#
# A function with two plain formal parameters and *args.
def f4(arg1, arg2, *args):
    print 'f4 -- arg1:', arg1
    print 'f4 -- arg2:', arg2
    print 'f4 -- *args:', args


#
# A function with two plain formal parameters and *args and **kwargs.
def f5(arg1, arg2, *args, **kwargs):
    print 'f5 -- arg1:', arg1
    print 'f5 -- arg2:', arg2
    print 'f5 -- args:', args
    print 'f5 -- kwargs:', kwargs


#
# A function with 4 default formal parameters.
# Try calling this function with a single keyword argument, accepting
#     the other default values.
def f6(arg1='default1', arg2='default2',
        arg3='default3', arg4='default4'):
    print 'f6 -- arg1:', arg1
    print 'f6 -- arg2:', arg2
    print 'f6 -- arg3:', arg3
    print 'f6 -- arg4:', arg4


#
# A function that takes a function and a collection as arguments.
# Apply the function (arg) to each item in the collection.
def f7(f, collection):
    for item in collection:
        f(item)

#
# Sample function to be passed to f7().
def f7a(element):
    print 'element * 3: %d' % (element * 3, )

#
# Print a horizontal rule.
def hr(msg):
    print '-' * 40
    print msg
    print '-' * 40


def test():
    hr('f1')
    print f1()
    hr('f2')
    f2('aaa', 'bbb', 'ccc')
    hr('f3-1')
    f3('aaaa', 'bbbb')
    hr('f-2')
    f3('aaaa', 'bbbb', 'cccc')
    hr('f-3')
    f3('aaaa', 'bbbb', arg4='dddd')
    hr('f4')
    f4('aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'ee')
    hr('f5-1')
    f5('aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'ee', argx='xx')
    hr('f5-1')
    f5(arg1='xx', arg2='yy', otherarg='zz')
    hr('f6')
    f6(arg2='zzzz')
    hr('f7')
    a1 = [11, 22, 33, 44, 55, ]
    f7(f7a, a1)
    hr('f2 -- with an "unrolled" argument list')
    a2 = [111, 222, 333, ]
    f2(*a2)


if __name__ == '__main__':
    test()
