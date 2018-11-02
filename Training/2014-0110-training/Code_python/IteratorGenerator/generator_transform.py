#!/usr/bin/env python
"""
filter_and_transform - filter_and_transform(content, test_fn, transform=None)

Return a generator that returns items from content after applying
the functions in transform if the item satisfies test_fn .

Arguments:

   1. ``values`` -- A list of values

   2. ``predicate`` -- A function that takes a single argument,
      performs a test on that value, and returns True or False.

   3. ``transform`` -- (optional) A list of functions.  Apply each
      function in this list and returns the resulting value.  So,
      for example, if the function is called like this::

          result = filter_and_transform[11, 22], p, [f, g])

      then the resulting generator might return::

          g(f(11))

"""


def filter_and_transform(content, test_fn, transform=None):
    for item in content:
        if test_fn(item):
            if transform is None:
                yield item
            elif isiterable(transform):
                for func in transform:
                    item = func(item)
                    yield item
            else:
                yield transform(item)


def isiterable(item):
    flag = True
    try:
        item = iter(item)
    except TypeError:
        flag = False
    return flag


def iseven(n):
    return n % 2 == 0


def f(n):
    return n * 2


def g(n):
    return n ** 2


def test():
    data1 = [11, 22, 33, 44, 55, 66, 77, ]
    print 'A single transform:'
    for val in filter_and_transform(data1, iseven, f):
        print 'val: %d' % (val, )
    print '-' * 40
    print 'Multiple transforms:'
    for val in filter_and_transform(data1, iseven, [f, g]):
        print 'val: %d' % (val, )
    print '-' * 40
    print 'Multiple transforms using lambda:'
    for val in filter_and_transform(
        data1,
        iseven,
        [
            lambda x: x + 10,
            lambda x: x + 20,
            lambda x: x + 30,
        ]
    ):
        print 'val: %d' % (val, )
    print '-' * 40
    print 'Transform is None:'
    for val in filter_and_transform(data1, iseven):
        print 'val: %d' % (val, )


if __name__ == '__main__':
    test()
