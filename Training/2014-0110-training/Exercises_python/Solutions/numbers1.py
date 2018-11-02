
import math


def test():
    """Perform various operations on integers and floats.
    """
    a = 5
    b = 6
    c = 3.0
    d = 4.5
    print 'a, b, c, d:', a, b, c, d
    print 'a + b:', a + b
    print 'a * (c + d):', a * (c + d)
    print 'a * c + d:', a * c + d
    print 'a / b:', a / b
    print 'float(a) / b:', float(a) / b
    print 'a ** b:', a ** b
    print 'math.pow(a, b):', math.pow(a, b)


if __name__ == '__main__':
    test()
