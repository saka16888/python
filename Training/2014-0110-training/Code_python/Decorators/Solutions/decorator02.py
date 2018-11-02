#!/usr/bin/env python


def trace(msg, count):
    print 'Creating wrapper -- msg:', msg, 'count:', count

    def inner1(func):
        def inner2(*args, **kwargs):
            print '>> [%s:%s] args: %s' % (msg, func.__name__, args, )
            retval = func(*args, **kwargs)
            print '<< [%s]' % (msg, )
            return retval
        return inner2

    return inner1


@trace('tracing func1', 3)
def func1(x, y):
    print 'x:', x, 'y:', y
    result = func2((x, y))
    return result
#func1 = trace('tracing func1', 3)(func1)


@trace('tracing func2', 4)
def func2(content):
    print 'content:', content
    return content * 3


def test():
    print '-' * 40
    result = func1('aa', 'bb')
    print 'result:', result

if __name__ == '__main__':
    test()
