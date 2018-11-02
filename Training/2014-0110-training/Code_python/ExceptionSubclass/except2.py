#!/usr/bin/env python


class MyExp(Exception):
    pass


def fn3():
    y = 3
    x = y
    print x
    print '(fn3) before raising exception'
    raise MyExp('fn3 raises an exception')
    print '(fn3) after raising exception'


def fn2():
    fn3()


def fn1():
    fn2()


def main():
    try:
        print '(main) before calling fn1'
        fn1()
        print '(main) after calling fn1'
    except MyExp as exp:
    # except (MyExp, NameError) as exp:
        print 'main caught this:', exp

main()
