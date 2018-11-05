from operator import itemgetter, attrgetter

a = [3, 6, 8, 2, 78, 1, 23, 45, 9]
print(sorted(a))
print(a.sort())
print(sorted(a,reverse=True))
print(a.sort(reverse=True))
b=[24,31]
print(a.extend(b))
print("a =",a)
print(a.extend([b]))
print("a =",a)
print(a.pop())
print("a =",a)


t = (3, 6, 8, 2, 78, 1, 23, 45, 9)
print("t =", sorted(t), list(sorted(t)))

'''
Since tuples are arrays that you cannot modify,
they don't have an in-place sort function that can be called directly on them.
They must always use the sorted function to return a sorted list.
'''

# print(sorted(a))  : AttributeError: 'tuple' object has no attribute 'sort'
print("Reverse sort t =", sorted(t, reverse=True))

#-------------------------------------------------------------
s1 = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'C', 10)]

def getKey(item):
    return item[1]


print(sorted(s1))
print(sorted(s1,key=lambda x : x[2]))
print(sorted(s1,key=getKey))
print("s1 itemgetter(1) = ", sorted(s1,key=itemgetter(1)))
print("s1 itemgetter(2) = ", sorted(s1,key=itemgetter(2)))
print("s1 itemgetter(0) = ", sorted(s1,key=itemgetter(0)))

'''
In Py3.0, the cmp parameter was removed entirely
as part of a larger effort to simplify and unify the language
eliminating the conflict between rich comparisons and the __cmp__ methods)
'''
# print(sorted(s1,c lambda x,y : cmp(x[2], y[2])))

#-------------------------------------------------------------
# dictionary
a1={1: 'D', 6: 'C', 3: 'B', 4: 'E', 5: 'A'}
print("sorted(a1) = ",sorted(a1))
# print("sorted(a1) = ",sorted(a1,itemgetter(1)))
print("a1[1]=",a1[1])
print("a1[1]=",a1.get(1))
print("a1 keys=",a1.keys())

# sort dict
# sort by key
for key in sorted(a1.keys()):
    print("Sort by keys %s: %s" % (key, a1[key]))
#sort by value
print("a1.items() =", a1.items())
for key,value in sorted(a1.items(), key=itemgetter(0)):
    print("Sort by key %s: %s" % (key, value))
for key,value in sorted(a1.items(), key=itemgetter(0),reverse = True):
    print("Reverse Sort by key %s: %s" % (key, value))
for key,value in sorted(a1.items(), key=itemgetter(1)):
    print("Sort by value %s: %s" % (key, value))


#----------------------------------------------------------------------
def fruitfunc():
    print("this is fruit")

def vegefunc():
    print("this is vege")

lookup={'fruit': fruitfunc, 'vege': vegefunc}
lookup.get('fruit')
print("a1 keys=",a1.keys())