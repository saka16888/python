'''
Apply function of two arguments cumulatively to the items of iterable,
from left to right,
so as to reduce the iterable to a single value.
For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
calculates ((((1+2)+3)+4)+5).
The left argument, x, is the accumulated value and the right argument,
y, is the update value from the iterable.
If the optional initializer is present, it is placed before the items of the iterable in the calculation,
and serves as a default when the iterable is empty.
If initializer is not given and iterable contains only one item, the first item is returned.
'''

from functools import reduce

mlist = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x + y, mlist))


def add(x, y):
    return x + y


print("reduce(add, mlist) = ", reduce(add, mlist))


def sq(x):
    return x * x


print(list(map(sq, range(1, 11))))


def double(x):
    return x + x


print(list(map(double, "abcd")))


def add(x, y): return x + y


print(list(map(add, range(8), range(8))))

print(reduce(add, range(1, 11)))  # sum 1~10
# n!
n = 3
print(reduce(lambda x, y: x * y, range(1, n + 1)))  # sum 1~10
n_fact = reduce(lambda x, y: x * y, range(1, n + 1))
print("%d!= %d" % (n, n_fact))
