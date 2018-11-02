
Count = 0
Sizes = []


def set_count1(x, y):
    Count = x ** 2 + y + 1
    Sizes.append(x)
    print 'Count: %d' % Count


def set_count2(x, y):
    global Count
    Count = x ** 2 + y + 1
    #print 'Count: %d' % Count


def test():
    print '1:', Count
    Count = 5
    set_count1(5, 8)
    print '2:', Count
    set_count2(5, 10)
    print '3:', Count

test()
