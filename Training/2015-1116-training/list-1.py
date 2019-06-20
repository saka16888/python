'''
    mutable sequence types
'''
#-------------------------------------------

s=[10,20,30]
t=s
print(id(s),id(t))
s.extend([40,50,40])
print(s)
print(id(s),id(t))

print("*" * 60)
s[3]=53
print("s[3] = ", s[3])
s.append(5)
s.append([6,7])
print("s[0:5] = ", s[0:5])
print("s[0:8:2] = ", s[0:8:2])
t=s[0:8:2]
print("s=",s, ", t=",t)
print(id(s),"\n",id(t))
print(s,s.count(40))
s.append("a")
print(s,s.count('a'))
print(s,s.count([6,7]))
print(s,s.count([10,20,30]))

s.extend([8,9])
s += [11,12] # equal extend
print("s =",s)
s.insert(2,'insert-2')
s*=2

if s:
    print("\ns  *= 2 , \nresult = ", s)

# delete sub list
del s[5:10]
print("del s[5:10], s =",s)

#s.remove("insert-2")
#print("s.remove(x)",s)
print("*" * 60)

try:
    s.remove("insert-2")
    print("s.remove(x)",s)
except:
    #pass
    print("s does not element ",x)

t1=[3,4,5]
s2=s.copy()
print(s,
      "\nindex of 40",s.index(40),
      "\ns2 = ",s2
      )
print("id(s) =  ",id(s),"\nid(s2) = ",id(s2))
#-------------------------------------------
print("*" * 60)
for i in s:
    print("i = ",i, ", type=",type(i))
    if type(i) == int:
        s.remove(i)
        print("remove ",i, ", s=",s)
    elif type(i) == str:
        #i='ss'
        i.upper()
        s[s.index(i)]=i.upper()
        print("Modify ", i, ", s=", s)
    elif type(i) == list:
        print("Pop ", i, ", s=", s.pop(i))

print("s=",s)
print("set(s) = ",set(s))

y=[[x,s.count(x)] for x in set(s)]
print("y =",y)

'''
for val,count in y:
    if s.count(x) > max_count:
        max_count=s.count(x)
        print(x,s.count(x))
        max_list.append([x,max_count])
print(max_list)
'''
