#
# Python 3 only
#
# yield, next, and send
#


def f(x):
    print('x:', x)
    x = yield x * 2
    print('x:', x)
    x = yield x * 2
    print('x:', x)
    x = yield x * 2
    print('x:', x)


def test():
    g = f(3)
    next(g)
    g.send(4)
    print('back in test 1')
    g.send(5)
    print('back in test 2')
    g.send(6)


test()
