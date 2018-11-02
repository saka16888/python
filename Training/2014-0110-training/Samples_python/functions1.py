"""
Define functions with several types of arguments and call them.
"""

def hr():
    print('-' * 60)

def f1(x, y):
    print('f1:', x, y)

def f2(x, y='abc', z=None):
    if z is None:
        z = []
    z.append(x)
    z.count(x)
    print('f2:', x, y, z, z.count(x))
    print('pop ',z.pop(len(z)-1))
    return z

def f3(x, y, *args, **kwargs):
    print('f3 -- x: %s  y: %s' % (x, y))
    print('f3 -- args:', args)
    print('f3 -- kwargs:', kwargs)
    return x + y, x * 3

def f4(*args, **kwargs):
    print('f4 -- args:', args)
    print('f4 -- kwargs:', kwargs)

def f5(*args, **kwargs):
    print('f5 -- starting')
    f4(*args, **kwargs)
    print('f5 -- leaving')

def show_args(x, *args, **kwargs):
    print('x     : %s' % (x, ))
    print('args  : %s' % (args, ))
    print('kwargs: %s' % (kwargs, ))

def show_args_helper(*args, **kwargs):
    print('helper starting')
    show_args(*args, **kwargs)
    print('helper leaving')

def test_args():
    show_args(11, 22)
    hr()
    show_args(x=111)
    hr()
    show_args(1111, 2222, 3333, arg1=4444, arg2=5555)
    hr()
    show_args_helper(1111, 2222, 3333, arg1=4444, arg2=5555)

def test():
    f1(5, 6)
    f1(y=6, x=5)
    hr()

    z = f2('aaa', 'bbb')
    print('z:', z)
    z = f2('ccc')
    print('z:', z)
    #z = f2('ddd', 'abc', [111, 222,])
    z = f2('ddd', z=[111, 222,])
    print('z:', z)

    hr()
    f3('aaa', 'bbb', 'ccc', 'ddd', arg1='eee', arg2='fff')

    hr()
    f5(11, 22, 33)
    f5(11, 22, width=33, height=44)

    hr()
    test_args()

if __name__ == '__main__':
    test()
    help(functions1)
