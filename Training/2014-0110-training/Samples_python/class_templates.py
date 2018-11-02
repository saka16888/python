
class Class1(object):
    """An empty class."""
    pass


class Class2(object):
    """A class with a constructor."""
    def __init__(self, ratio):
        self.ratio = ratio
        self.size = None

    def display(self):
        print '(Class2) ratio: %s' % self.ratio


class Class3(Class2):
    """A subclass with a constructor and one additional method."""

    def __init__(self, ratio, base_quantity):
        super(Class3, self).__init__(ratio)
        #Class2.__init__(self, ratio)
        self.base_quantity = base_quantity

    def display(self):
        super(Class3, self).display()
        #Class2.display(self)
        print '(Class2) base_quantity: %s' % self.base_quantity

    def update(self, new_base_quantity):
        self.base_quantity += new_base_quantity
        self.display()


class Class4(object):
    """A class with a constructor and a property."""
    def __init__(self, ratio, size):
        self.ratio = ratio
        self._size = size

    def display(self):
        """Display this object."""
        print '(Class4) ratio: %s  size: %s' % (self.ratio, self._size, )

    def _get_size(self):
        print 'called _get_size'
        return self._size

    def _set_size(self, size):
        print 'called _set_size'
        self._size = size

    def _del_size(self):
        print 'called _del_size'
        del self._size

    size = property(_get_size, _set_size, _del_size, "size property docstring")


def test():
    obj1 = Class3(3, 5)
    obj1.display()
    print '-' * 20
    obj1.update(4)
    print '-' * 20
    # test the property.
    obj2 = Class4(4.5, 6)
    obj2.display()
    print 'obj2.size:', obj2.size
    obj2.size = 7
    obj2.display()
    print 'hasattr "size":',  hasattr(obj2, 'size')
    del obj2.size
    print '---'
    print 'hasattr "size":',  hasattr(obj2, 'size')


if __name__ == '__main__':
    test()
