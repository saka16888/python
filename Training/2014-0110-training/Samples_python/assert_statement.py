"""
Synopsis:
    Demonstrate use of the assert statement.
Usage:
    Run this script both with and without the "-O" command line
    option.
Examples:
    $ python assert_statement.py
    $ python -O assert_statement.py
"""


HerbTable = {
    4: 'parsley',
    8: 'cilantro',
    12: 'tarragon',
    16: 'basil',
    17: 'red basil',
}


def validate(value):
    """A sample validation function.
            Return True if value is even and value is in HerbTable.
        """
    if (value % 2 == 0 and
        value in HerbTable):
        return True
    return False


def test(value):
    #assert value % 2 == 0
    assert validate(value), "value must be even and must be in HerbTable"
    herbname = HerbTable[value]
    print('valid value -- %s/%s' % (value, herbname, ))


def main():
    print('__debug__:', __debug__)
    test(4)
    test(12)
    test(2)
    test(3)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
