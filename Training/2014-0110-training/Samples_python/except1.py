import sys

#Collection = [11, 22]

print sys.path

class LightError(Exception):
    pass


def inner(collection, idx):
    return collection[idx]

def inner1(collection, idx):
    raise LightError, 'this exception is lightweight'
    raise LightError('this exception is lightweight')
    try:
        print 'inner1'
        return inner(collection, idx)
    except IndexError, exp1:
        print 'this index is bad'
        raise

def outer():
    global Collection
    Collection = 'the big collection'
    names = ['dave', 'wen-chi',]
    print 'starting'
    try:
        #x = abc
        print 'before exception'
        item = inner1(names, 4)
        print 'name: %s' % (item, )
    except IndexError, exp1:
        print 'bad index -- "%s"' % exp1
        print 'exp1.args: %s' % (exp1.args, )
        print 'exp1.__class__: %s' % (exp1.__class__, )
    except LightError, exp1:
        print 'what the?  an error? -- %s' % exp1
    except NameError, exp1:
        print 'a name error'
    print 'leaving'


if __name__ == '__main__':
    outer()

