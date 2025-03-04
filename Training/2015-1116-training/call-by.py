def f1(x):
    x=9
    return x

def s1(x):
    x="abc"
    return x


def f2(x):
    x=[1,2,3]
    return x

def f3(x):
    x.extend([1,2,3])
    return x

a=2
print("Call by value %r , %r" % (f1(a),a))

s="cdf"
print("Call by value %r , %r" % (s1(s),s))

b=[9,8]
print("Call by reference %r , %r" % (f2(b),b))

c=[9,8]
print("Call by reference %r , %r" % (f3(c),c))
