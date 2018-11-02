class TestProperty(object):
    def __init__(self, description):
        self._description = description

    @property
    def description(self):
        print 'getting description'
        return self._description

    @description.setter
    def description(self, description):
        print 'setting description'
        self._description = description


def test():
    obj = TestProperty('some description')
    print '"%s"' % obj.description
    print '-' * 40
    obj.description = 'new description'
    print '"%s"' % obj.description


test()
