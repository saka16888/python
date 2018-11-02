def f(x, y):
    print 'x:', x
    print 'y:', y


def g(x=1, y=2, z=3):
    print 'x:', x
    print 'y:', y
    print 'z:', z
    #print w


def display_args(size, *args, **kwargs):
    print size
    print args
    print kwargs

def add1(x, accum=[]):
    accum.append(x)
    return accumdef add1(x, accum=[]):
    accum.append(x)
    return accum


def add2(x, accum=None):
    if accum is None:
        accum = []
    accum.append(x)
    return accum
