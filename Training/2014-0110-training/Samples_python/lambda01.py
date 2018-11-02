"""
Demonstrate use of lambdas.
Compare with use of regular functions.
"""

#
# Map names to lambdas.
Funcs1 = {
    'double': lambda x: x * 2,
    'triple': lambda x: x * 3,
    'complex': lambda x: double(x) + triple(x),
}


def double(x):
    return x * 2


def triple(x):
    return x * 3


def complex(x):
    return double(x) + triple(x)

#
# Map names to functions.
Funcs2 = {
    'double': double,
    'triple': triple,
    'complex': complex,
}


def test():
    print 'double:', Funcs1['double'](5)
    print 'triple:', Funcs1['triple'](5)
    print 'complex:', Funcs1['complex'](5)
    print '-' * 40
    print 'double:', Funcs2['double'](5)
    print 'triple:', Funcs2['triple'](5)
    print 'complex:', Funcs2['complex'](5)


test()
