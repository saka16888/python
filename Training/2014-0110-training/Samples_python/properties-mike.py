class TestProperty(object):

    def __init__(self, description):
        self._description = description
        self.__size = 5

    def _set_description(self, description):
        print 'setting description'
        self._description = description

    def _get_description(self):
        print 'getting description'
        return self._description

    def _add_description(self, description):
        print 'add description'
        self._description = "add" + description

    description = property(_get_description, _set_description, _add_description)

def test():
    obj = TestProperty('some description')
    print '"%s"' % obj.description
    print '-' * 40
    obj.description = '1234567890'
    print '"%s"' % obj.description


test()
