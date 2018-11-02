class TestProperty(object):

    def __init__(self, description):
        self._description = description
        self.__size = 25

    def _set_description(self, description):
        print 'setting description'
        self._description = description

    def _get_description(self):
        print 'getting description'
        return self._description

    description = property(_get_description, _set_description)
