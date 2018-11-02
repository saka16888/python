#!/usr/bin/env python


def wrapper(fn):
    def inner_fn(*args, **kwargs):
        print '>> [%s]' % (fn.__name__, )
        result = fn(*args, **kwargs)
        print '<< [%s]' % (fn.__name__, )
        return result
    return inner_fn


@wrapper
def fn1(msg):
    #print '(fn1) before.  msg:', msg
    result = fn2(msg)
    #print '(fn1) after.  msg:', msg
    return result
## fn1 = wrapper(fn1)


@wrapper
def fn2(msg):
    #print '(fn2) before.  msg:', msg
    result = msg.upper()
    #print '(fn2) after.  msg:', msg
    return result


def test():
    print fn1('a simple message')


if __name__ == '__main__':
    test()
