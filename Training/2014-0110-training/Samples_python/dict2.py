"""
Create several dictionaries and display the items in them.

Create:
- an empty dictionary.
- a dictionary with strings as keys and integers as values.
- a dictionary with strings as keys and lists of integers as values.
Display the items in the dictionaries.
"""

D1 = {}
D2 = {
    'aa': 111,
    'bb': 222,
    'cc': 333,
    }

D3 = {
    'apple': [11, 22, 33,],
    'banana': [44, 55, 66,],
    }


def test1():
    for key in D2.keys():
        print 'key: %s' % key

def test2():
    for value in D2.values():
        print 'value: %s' % value

def test3():
    for key in D3.keys():
        print 'key: %s' % key
        for item in D3[key]:
            print '    item: %d' % item

def test4():
    for key, value in D3.items():
        print 'key: %s' % key
        for item in value:
            print '    item: %d' % item

def hr():
    print '-' * 40

def test():
    test1()
    hr()
    test2()
    hr()
    test3()
    hr()
    test4()

if __name__ == '__main__':
    test()

