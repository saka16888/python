
x=0b11111111
print('x= %d' % x)

z=5+5
print('z = %d' % z)

a=int('11',base=2)
print('a = %d' % a)

n = 37
print('n = %s' % bin(n))
#print('n = %d' % bin(n))
print("-" * 40)
print("%d" % (2^3))
print("%d" % (2**3))
print("%d" % (3<<3))
print("%d" % (5/3))

a=5/3
print("a= %f" % a)
a=2/3
print("a= %f" % a)
a=2.0/3
print("a= %f" % a)
a=-2/3
print("a= %f" % a)
a=-2.0//3
print("a= %f" % a)
a=-2.0/(-3)
print("a= %f" % a)
a=-2.0//(-3)
print("a= %f" % a)

st = '123'
binSt = ' '.join(format(ord(x), '08b') for x in st)
print(binSt)

add = lambda x,y : x + y
#reduce(add, [int(x) * 2 ** y for x, y in zip(list(binstr), range(len(binstr) - 1, -1, -1))])

