__author__ = 'mihung'


lambda x:x*x (15)
x=5
list(map(lambda x : x*x, [1,2,3]))

f = lambda x: (lambda y: x+y)

def f(s=None):
    print(s or 'Missing')

f('Hello')
f('')

s = [10,20,30,40]
t = {10,20,30,40}

if (10 in s):
    print("yes")

if (10 in t):
    print("yes")

