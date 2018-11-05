s1='sdvvsvkv'
t1="sif"
s = set(s1)
t = set(t1)

print("s = ",s, " s.difference(t1) = " ,s.difference(t1))
print("t = ",t)

u1=['a','b','c']
u = set(u1)
print('u = ',u)

u2="ABCDREGfsd"
u22 = set(u2)
print('u22 = ',u22)

print('s.union(t)', s.union(t))
print('s.intersection(t)', s.intersection(t))
print('s.intersection(u)', s.intersection(u))
print('s.difference(t)', s.difference(t))
print('t.difference(s)', t.difference(s))

intersect= s & t
print("(s & t) = %r" % (s & t))
print("(s & t) intersect = %r" % intersect)
print(s | t)
print(s - t)

setA = {1,2,3,4,5,6}
setB = {2,3,4,5,6,7,8}
print(setA.union(setB),len(setA.union(setB)))

zipped=zip(setA,setB)
print(list(zipped))
