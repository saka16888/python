
DEBUG = False


def dbgprint(msg):
    if DEBUG:
        print msg


class ParameterizedProperty(object):
    """Emulate PyProperty_Type() in Objects/descrobject.c
    Parameterize the property so that we can reuse getters and setters
        for properties with different names.
    Reference: See the section on properties in the "Descriptor HowTo Guide":
        http://docs.python.org/2/howto/descriptor.html#properties
    """

    def __init__(self, attrname, fget=None, fset=None, fdel=None, doc=None):
        self.attrname = attrname
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj, self.attrname)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, self.attrname, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj, self.attrname)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)


# A function to make use of ParameterizedProperty class seem more
#     like the use of the property builtin function.
def paramprop(*args, **kwargs):
    return ParameterizedProperty(*args, **kwargs)


ColorLabel2rgb = {
    'red': 0xff0000,
    'green': 0x00ff00,
    'blue': 0x0000ff,
}

# Invert the table so that we can lookup by RGB color number.
ColorRgb2label = dict(((b, a) for (a, b) in ColorLabel2rgb.iteritems()))


class ColorScreen(object):
    """A color screen class that supports properties for:
           - background color
           - foreground color
           - highlight background color
           - highlight foreground color
    This class demonstrates the use of parameterized properties.  These
        are similar to normal Python properties, but enable us to reuse the
        same getter and setter methods for multiple, similar instance
        variables.
    Things to note -- Although there are 4 properties, there is only
        one getter method and one setter method.
    """
    def __init__(self, bgcolor, fgcolor, hibgcolor, hifgcolor):
        self._bgcolor = ColorLabel2rgb.get(bgcolor, bgcolor)
        self._fgcolor = ColorLabel2rgb.get(fgcolor, fgcolor)
        self._hibgcolor = ColorLabel2rgb.get(hibgcolor, hibgcolor)
        self._hifgcolor = ColorLabel2rgb.get(hifgcolor, hifgcolor)

    def _getcolor(self, attrname):
        value = getattr(self, attrname, None)
        dbgprint('1. getting: %s' % value)
        if value in ColorRgb2label:
            value = ColorRgb2label[value]
        dbgprint('2. getting: %s' % value)
        return value

    def _setcolor(self, attrname, value):
        dbgprint('1. setting: %s' % value)
        if value in ColorLabel2rgb:
            value = ColorLabel2rgb[value]
        dbgprint('2. setting: %s' % value)
        setattr(self, attrname, value)

    bgcolor = paramprop('_bgcolor', _getcolor, _setcolor)
    fgcolor = paramprop('_fgcolor', _getcolor, _setcolor)
    fgcolor = paramprop('_hibgcolor', _getcolor, _setcolor)
    fgcolor = paramprop('_hifgcolor', _getcolor, _setcolor)


def test():
    s1 = ColorScreen(2, 3, 4, 5)
    s2 = ColorScreen(22, 33, 44, 55)
    print '-----'
    v1 = s1.bgcolor
    v2 = s1.fgcolor
    print 'A.', v1, v2
    v1 = s2.bgcolor
    v2 = s2.fgcolor
    print 'A.', v1, v2
    print '-----'
    s1.bgcolor = 'red'
    s1.fgcolor = 'blue'
    s2.bgcolor = 'green'
    s2.fgcolor = 'yellow'
    v1 = s1.bgcolor
    v2 = s1.fgcolor
    print 'B.', v1, v2
    v1 = s2.bgcolor
    v2 = s2.fgcolor
    print 'B.', v1, v2
    print '-----'
    s1.bgcolor = 0xff0000
    s1.fgcolor = 0x00ff00
    s2.bgcolor = 0x0000ff
    s2.fgcolor = 'red'
    v1 = s1.bgcolor
    v2 = s1.fgcolor
    print 'C.', v1, v2
    v1 = s2.bgcolor
    v2 = s2.fgcolor
    print 'C.', v1, v2


if __name__ == '__main__':
    test()
