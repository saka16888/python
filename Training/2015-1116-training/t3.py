__author__ = 'mihung'

import os

int1="0/3"
cmd=["int 0/1",
     "shutdown"]
for i in cmd:
    print("line: ",i)

cmd=[int1,"shutdown"]
for i in cmd:
    print("line: ",i)

cmd={'shutdown', 'int 0/2'}
for i in cmd:
    print("line: ",i)

s = set('sdvvsvv')
t = set('siemvmevf')

s.union(t)
s.intersection(t)
s.difference(t)
t.difference(s)

print("%r" % (s & t))
print(s | t)
print(s - t)

even = [2, 4, 6, 8]
prime = [2, 3, 5, 7, 11]

print(min(even))
#all = even.append(prime)
#print(all)
all = even + prime
print(all)
#print(even - prime)

tmp=sorted(set(dir(list)) - set(dir(tuple)))
print(tmp)

#print(all[0])
print(all[-1])
print(sum(all))
print(min(all))
print(max(all))

print('count:', even.count(4), even.count(2))
