
"""
Create several collections and use a for statement to display the items in them.
"""

import types

Dict1 = {
    'aa': 111,
    'bb': 222,
    'cc': 333,
    }

Collection = [123, 'aaa', [11, 22], Dict1, ]

def test1(collection):
    for item in collection:
        if type(item) is types.StringType:
            break
        if type(item) is types.IntType:
            print '%s is an integer' % item
        elif type(item) is types.StringType:
            print '%s is an string' % item
        elif type(item) is types.ListType:
            print '%s is a list' % item
            test(item)
        else:
            print '%s is none of the above' % item

def test2(collection):
    while collection:
        item = collection.pop()
        print item

def hr():
    print '-' * 40

def main():
    test1(Collection)
    hr()
    test2(Collection)
    hr()
    test2(Collection)


if __name__ == '__main__':
    main()
