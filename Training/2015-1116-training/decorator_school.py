__author__ = 'mihung'
'Learn how PyATS decorators work in principle'

def mygetattr(obj, attr, default):
    'Return the attribute value if it exists or the default'
    return obj.__dict__[attr] if attr in obj.__dict__ else default

class F:
    pass

def square(x):
    return x ** 2

square.happy = True

def cube(x):
    return x ** 3

cube.cool = True
cube.loop = 3

def collatz(x):
    return 3*x + 1 if x % 2 else x // 2

collatz.happy = True
collatz.cool = True

f = F()
print(dir(f))
f.color = 'blue'
f.width = 20

funcs = [square, cube, collatz]
for func in funcs:
    print(func.__name__, func(10))


mygetattr(square,'happy',True)
mygetattr(square,'happy',False)
mygetattr(square,'cool',False)
mygetattr(cube,'Loop',1)
mygetattr(square,'Loop',1)