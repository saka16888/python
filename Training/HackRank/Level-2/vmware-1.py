
a=[1,3,5,100,1002]
s1=set(a)
s2={i for i in s1 if (i <1000) and (i>0)}
print(s2)
print(sorted(list(s2)))