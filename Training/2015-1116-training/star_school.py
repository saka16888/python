'Goal:  Learn fundamental Python argument passing techniques'

def mypow(base, exp):
    'Raise base to the power of exp'
    return base ** exp

print(mypow(2, 5))                              # positional arguments --> order matters
print(mypow(exp=5, base=2))                     # keyword arguments -> na#me matters
print(mypow(2, exp=5))                          # hybrid arguments -> positional arguments go before keyword arguments
# print(mypow(base=2,5))                                                       # SyntaxError: non-keyword arg after keyword arg

print(mypow(0,5))
#print(mypow(2,'hello'))

arguments = (2, 5)                                # cheap suitcase, tuples are compact and fast
print(mypow(arguments[0], arguments[1]))          # need to unpack BEFORE you make the function call
print(mypow(*arguments))                          # one star UNPACKS a SEQUENCE into POSITIONAL arguments

arguments = {'exp': 5, 'base': 2}                 # expensive suitcase, dicts are spare structures and incur hashing time
print(mypow(exp=arguments['exp'], base=arguments['base']))   # need to unpack BEFORE you make the function call
print(mypow(**arguments))

arguments = {'base': 2, 'exp': 5}                 # expensive suitcase, dicts are spare structures and incur hashing time
print(mypow(exp=arguments['exp'], base=arguments['base']))   # need to unpack BEFORE you make the function call
print(mypow(**arguments))

def f(a, b, c=0):                                 # optional arguments have default values and FOLLOW required arguments
    return a + b + c

print(f(10,5))
print(f(10,5,1))

def f(a, b, c=0, d=0):                            # optional arguments have default values and FOLLOW required arguments
    return a + b + c + d

def f(a, b, *args):         # 1-stars packs variable length positional args into a tuple
    print(a)
    print(b)
    print(args)
f(10,5,1,20)


def f(a, b, *args, **kwargs):                     # variable length argument lists in python
    print(a)
    print(b)
    print(args)                                   # 1-stars packs variable length positional args into a tuple
    print(kwargs)                                 # 2-stars packs variable length keywords args into a dict

f(13,6,2,20)



