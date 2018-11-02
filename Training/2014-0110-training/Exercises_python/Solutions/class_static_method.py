import time

class TestClass(object):
    """A class that tests (1) a class variable, (2) a class method,
    and (3) a static method.
    """
    class_description = "A test for class methods and static methods"

    @classmethod
    def show_description(cls):
        print('description: %s' % cls.class_description)
    ## show_description = classmethod(show_description)

    @staticmethod
    def show_time():
        print('current time: "%s"' % time.ctime())
    ## show_time = staticmethod(show_time)

def test():
    TestClass.show_description()
    TestClass.show_time()
    TestClass.class_description = 'another description'
    TestClass.show_description()

test()
