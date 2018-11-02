def gen1(x, y):
    print 'one'
    yield x * 2
    print 'two'
    yield y * 3
    print 'three'

def gen2(container):
        for item in container:
            if item % 2 == 0:
                yield item * 3

def test():
    for item in gen1(5, 10):
        print 'item:', item
    print '-' * 40
    for item in gen2([11, 22, 33, 44]):
        print 'item:', item

test()
