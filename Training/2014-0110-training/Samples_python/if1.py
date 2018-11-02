"""
Demonstrate several forms of the if statement.

1. Create a dictionary.
2. For each item in the dictionary, test its value for one of 
   the following:
    - None
    - 'abc'
    - 0
    - the empty string
3. Print out a message for each case.
"""

Dict1 = {
    'key1': 'abc',
    'key2': None,
    'key3': '',
    'key4': 0,
    'key5': 'xyz'
    }


def test():
##     for key in Dict1:
##         value = Dict1[key]
    for key, value in Dict1.items():
        if value is None:
            print('the value of %s is nothing' % (key, ))
        elif value == 'abc':
            print('the value of %s is the string "abc"' % (key,))
        elif value == 0:
            print('the value of %s is zero' % (key, ))
        elif value == '':
            print('the value of %s is the empty string' % (key,))
        else:
            print('none of the above -- key: %s  value: %s'
                 % (key, value,))
    print('-' * 40)
    for key, value in Dict1.items():
        if value is None:
            print('the value of %s is nothing' % (key, ))
        elif value == 'abc' or value == '':
            print('the value of %s is the string "abc" or empty (%s)' % (
            key, value, ))
        elif value == 0:
            print('the value of %s is zero' % (key, ))
        else:
            print('none of the above -- key: %s  value: %s' % (key, value,))

if __name__ == '__main__':
    test()


