"""
Demonstrate use of try: statement.
In particular with the else: and finally: clauses.
"""


def test():
    try:
        open('abcdefg.txt', 'r')
    except IOError as exptn:
        print '1. caught error --', exptn
    else:
        print '1. just checking'

    print '-' * 20
    try:
        infile = open('try_finally.py', 'r')
        infile.close()
    except (IOError, ValueError, ImportError) as exptn:
        print '2.', exptn
    else:
        print '2. opened try_finally.py OK'

    print '-' * 20
    try:
        print '3. OK so far'
    finally:
        print '3. things are good'

    print '-' * 20
    try:
        print 1 / 0
    finally:
        print '4. there is a problem'


if __name__ == '__main__':
    test()
