
def test():
    """Perform various operations on lists."""
    value1 = []
    print 'An empty list: %s' % (value1, )
    value2 = [11, 22, 'aa', 'bb']
    print 'Another list: %s' % (value2, )
    value2.append('cc')
    print 'After append: %s' % (value2, )
    value2.insert(0, -1)
    print 'After insert: %s' % (value2, )
    print 'Length: %d' % (len(value2), )
    print 'The second element: %s' % (value2[1], )
    print 'A slice: %s' % (value2[1:3], )
    value3 = [33, 22, 11]
    value4 = [66, 55, 44]
    value5 = value3 + value4
    print 'Combined lists: %s' % (value5, )
    value5 += [88, 77]
    print 'Augmented list: %s' % (value5, )
    value5.sort()
    print 'Sorted list: %s' % (value5, )
    value6 = ("abcd", )    # Or just -- "abcd".  Parentheses optional.
    print 'One element tuple: %s' % (value6, )
    value6 = 111, 222, 333
    print 'Multiple element tuple: %s' % (value6, )
    data1 = ['aa', 11, 'bb', 22, 'cc', 33, 'dd', 44]
##     data2 = [(data1[idx], data1[idx+1]) for idx in range(0, len(data1), 2)]
    data2 = []
    for idx in range(0, len(data1), 2):
        data2.append((data1[idx], data1[idx+1]))
    print 'data1:', data1
    print 'data2:', data2
    data3 = [11, 22, 33, 44, 55, 66, 77, 88]
    data4 = sorted(data3, cmp_odd_even)
    print 'data3:', data3
    print 'data4:', data4


def apply(fn, numbers):
    accum = []
    for num in numbers:
        accum.append(fn(num))
    return accum


#
# Return the following:
#
#  a      b      Return
#  -----  -----  --------
#  Even   Even   0
#  Even   Odd    +1
#  Odd    Even   -1
#  Odd    Odd    0
#
def cmp_odd_even(a, b):
    if a % 2 == 0:
        if b % 2 == 0:
            return 0
        else:
            return 1
    else:
        if b % 2 == 0:
            return -1
        else:
            return 0


def fn1(x):
    return x * 3


def main():
    test()
    accum = apply(fn1, [11, 22, 33, 44])
    print 'accum (after applying fn1):', accum


main()
