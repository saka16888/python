
SharedValue = 'initial'


def set_value(x):
    global SharedValue
    SharedValue = x
    return SharedValue


def test():
    print 'SharedValue:', SharedValue
    set_value('updated')
    print 'SharedValue:', SharedValue


test()
