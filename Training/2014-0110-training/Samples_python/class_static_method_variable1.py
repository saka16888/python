class TestClass(object):
    """A demonstration of various class features.

    - class variables
    - a class method
    - a static method
    """

    V1 = -1
    V2 = 'empty'

    def show_instance(self):
        """An instance method receives the instance as the first parameter."""
        print '(instance)  V1: %s  V2: %s' % (self.V1, self.V2, )
        # but cannot do the following because it creates an instance variable.
        #self.V1 = 25

    @classmethod
    def show_class(cls):
        """A class method receives the class as the first parameter."""
        print 'class:', cls
        print '(class)     V1: %s  V2: %s' % (cls.V1, cls.V2, )

    @staticmethod
    def show_static():
        """A staticmethod does not receive any *special* first parameter."""
        print('(static)    V1: %s  V2: %s' % (TestClass.V1, TestClass.V2, ))


class SubTestClass(TestClass):
    V1 = 50

##     @classmethod
##     def show_class(cls):
##         print 'class:', cls
##         print '(B/class)   V1: %s' % (cls.V1, )


def test():
    a1 = TestClass()
    TestClass.show_class()
    a1.show_instance()
    a1.show_static()
    TestClass.V1 = 12
    TestClass.V2 = 'full'
    print '-' * 40
    TestClass.show_class()
    a1.show_instance()
    a1.show_static()
    print '-' * 40
    TestClass.show_class()
    SubTestClass.show_class()


test()
