class A(type):
    def __new__(cls, name, bases, attrs):
        # this allows B().username to also work
        attrs['username'] = property(lambda s: s.__class__.username)
        return type.__new__(cls, name, bases, attrs)
    @property
    def username(self):
        if not hasattr(self, '_username'):
            self._username = 'bar'
        return self._username

class B(object):
    __metaclass__ = A

print(B.username)
print(B().username)

