def fn1(n):
    try:
        1 / n
    finally:
        print 'in finally clause'


def fn2(n):
    try:
        1 / n
    finally:
        print 'in finally clause'
        return

def fn3():
    try:
        pass
    except:
        pass


