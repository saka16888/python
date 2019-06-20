from functools import reduce

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        print("%d mod %d = %d " % (a,b,a%b))
        a, b = b, a % b
    return a

def gcdd(args):
    return reduce(gcd,args)

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(args):
    """Return lcm of args."""
    return reduce(lcm, args)

#n,m = input().strip().split(' ')
#n,m = [int(n),int(m)]
a=[33324]
b=[34]
# a = [int(a_temp) for a_temp in input().strip().split(' ')]
# b = [int(b_temp) for b_temp in input().strip().split(' ')]

x=lcmm(a)
y=gcdd(b)
print("x = ",x)
print("y = ",y)

count=0;
tmp=x
while (tmp <= y):
    if (y % tmp == 0):
        print ("tmp", tmp)
        count += 1
    tmp += x
print(count)
