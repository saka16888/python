s=(1,2,3,7,9,4,5,6,)
print(s.count(1))
print(s.index(3))
print(s.index(6))
print(s[2:3])

s1=set(s)
print(s1,dir(s1))
s1.add(6)
print(s1)
#print(sort(s1))
s1.add(4)
print(s1)
s1.add(8)
print(s1)
print(type(s1))

t=(8,9,)
level1 = (
         (1,1,1,1,1,1),
         (1,0,0,0,0,1),
         (1,0,0,0,0,1),
         (1,0,0,0,0,1),
         (1,0,0,0,0,1),
         (1,1,1,1,1,1))
list1=[y for y in [x for x in level1]]
print(list1)
