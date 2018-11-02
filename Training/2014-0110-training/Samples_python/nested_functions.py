def make_function(x):
    """Demo for nested function.  Return a function object."""
    y = x * 3

    def inner():
        print y
    return inner


def make_wrapper(banner, fn):
    """Create a wrappr function.  Return a function object."""
    def inner(*args, **kwargs):
        print '>>', banner
        return_value = fn(*args, **kwargs)
        print '<<', banner
        return return_value
    return inner


def sample_function(arg1, arg2):
    """A sample function to be used to demonstrate make_wrapper."""
    print 'arg1:', arg1
    print 'arg2:', arg2


def test():
    fn1 = make_function('hello')
    fn2 = make_function('goodbye')
    fn1()
    fn2()
    print '-*' * 20
    wrapper = make_wrapper('wrapper1', sample_function)
    wrapper('one', 'two')
    wrapper('three', 'four')
    wrapper = make_wrapper('wrapper2', sample_function)
    wrapper('one', 'two')
    wrapper('three', 'four')


if __name__ == '__main__':
    test()
