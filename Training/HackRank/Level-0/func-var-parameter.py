class Parent(object):
    def __init__(self, a, b):
        print('a', a)
        print('b', b)


class Child(Parent):
    def __init__(self, c, d, *args, **kwargs):
        print('c', c)
        print('d', d)
        for key in kwargs:
            print("another keyword arg: %s: %s" % (key, kwargs[key]))
        super(Child, self).__init__(*args, **kwargs)

test = Child(1, 2, 3, 4)

def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)
test_var_args('yasoob', 'python', 'eggs', 'test')

def myfunc(**kwargs):
    # kwargs is a dictionary.
    print(*kwargs)
    for k, v in kwargs.items():
        print("%s = %s" % (k, v))

myfunc(abc=123, efh=456)
