"""
Synopsis -- Tests for functions.
"""

#
# A global variable
LABEL = 'Initial value for LABEL'


# Exercise 1
def fn1(x, y):
    """Two plain paramenters -- return a tuple."""
    print 'fn1 --', x, y
    return x, y


# Exercise 2
def fn2(name, size=0):
    """One plain and one optional parameter -- return a tuple."""
    print 'fn2 -- name: %s  size: %d' % (name, size, )
    return name * 2, size * 2


# Exercise 3

# Wrong.
def fn3a(x, val=[]):
    val.append(x)
    print 'fn3a -- val:', val


# Right
def fn3b(x, val=None):
    """A parameter with a default value that is mutable (a list)."""
    if val is None:
        val = []
    val.append(x)
    print 'fn3b -- val:', val


# Exercise 4

#
# A function with two plain formal parameters and *args and **kwargs.
def fn4(arg1, arg2, *args, **kwargs):
    print 'fn4 -- arg1:', arg1
    print 'fn4 -- arg2:', arg2
    print 'fn4 -- args:', args
    print 'fn4 -- kwargs:', kwargs


# Exercise 5

# Wrong
def fn5a(new_value):
    LABEL = new_value
    print 'fn5 -- local LABEL: "%s"' % (LABEL, )


# Right
def fn5b(new_value):
    global LABEL
    LABEL = new_value


# Exercise 6

#
# A function with 4 default formal parameters.
# Try calling this function with a single keyword argument, accepting
#     the other default values.
def fn6(arg1='default1', arg2='default2',
        arg3='default3', arg4='default4'):
    print 'fn6 -- arg1:', arg1
    print 'fn6 -- arg2:', arg2
    print 'fn6 -- arg3:', arg3
    print 'fn6 -- arg4:', arg4


# Exercise 7

def produce_custom_function(color):
    """Create a function that prints a customized value."""

    def inner(size):
        print 'fn7 -- size: %d  color: %s' % (size, color, )

    return inner


def test():
    value = fn1('abc', 'def')
    print 'fn1 --', value
    value = fn2('apple')
    print 'fn2 --', value
    value = fn2('berry', 4)
    print 'fn2 --', value
    value = fn2(size=5, name='cherry')
    print 'fn2 --', value
    fn3a(11)
    fn3a(22)
    fn3a(33)
    fn3b(11)
    fn3b(22)
    fn3b(33)
    fn4(
        'plain arg1',
        'plain arg2',
        'addl arg1',
        'addl arg2',
        'addl arg3',
        key1='keyword arg1',
        key2='keyword arg2',
        key3='keyword arg3',
        )
    print 'fn5 -- LABEL (1): "%s"' % (LABEL, )
    fn5a("New value #2")
    print 'fn5 -- LABEL (2): "%s"' % (LABEL, )
    fn5b("New value #3")
    print 'fn5 -- LABEL (3): "%s"' % (LABEL, )
    fn6(arg2='a new value for arg2')
    fn7 = produce_custom_function('red')
    fn7(25)
    fn7 = produce_custom_function('green')
    fn7(35)


if __name__ == '__main__':
    test()
