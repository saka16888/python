'Learn how PyATS decorators work in principle'

def run_cool_functions(funcs, x):
    print('Running "cool" functions with %r' % x)
    for func in funcs:
        if getattr(func, 'cool', False):
            times = getattr(func, 'loop', 1)
            for i in range(times):
                print(func.__name__, func(x))
    print()

def run_happy_functions(funcs, x):
    print('Running "happy" functions with %r' % x)
    for func in funcs:
        if getattr(func, 'happy', False):
            times = getattr(func, 'loop', 1)
            for i in range(times):
                print(func.__name__, func(x))
    print()

def happy(func):
    func.happy = True
    return func

def cool(func):
    func.cool = True
    return func

def loop(times=1):
    def inner(func):
        func.loop = times
        return func
    return inner

################################################

@happy                        # square = happy(square)
def square(x):
    return x ** 2

@cool                         # cube = cool(cube)
@loop(3)                      # cube = loop(3)(cube)
def cube(x):
    return x ** 3

@cool                         # collatz = cool(collatz)
@happy                        # collatz = happy(collatz)
def collatz(x):
    return 3*x + 1 if x % 2 else x // 2

if __name__ == '__main__':
    funcs = [square, cube, collatz]
    run_cool_functions(funcs, 10)
    run_happy_functions(funcs, 20)

    dispatch= {
        'square': square,
        'cube':cube,
    }

    s = 'square'
    print(dispatch[s](5))
    s = 'cube'
    print(dispatch[s](5))

