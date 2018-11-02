# alternative style -- global statement before use of variable.
def set_globals1(x, y):
    print x, y
    global Gx
    Gx = x
    global Gy
    Gy = y


# alternative style -- global statement at beginning of the function.
def set_globals2(x, y):
    global Gx, Gy
    print x, y
    Gx = x
    Gy = y


# define a global variable
Gz = []


def set_globals3(x):
    # global statement not needed
    # global Gz
    Gz.append(x)


def test():
    set_globals1(11, 22)
    set_globals2(33, 44)
    set_globals3('aa')
    set_globals3('bb')
    set_globals3('cc')
    print 'Gz:', Gz


if __name__ == '__main__':
    test()
