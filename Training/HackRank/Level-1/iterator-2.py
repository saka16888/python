'''import re'''

x = iter([1, 2, 3])
print("x.__next__() = ",x.__next__())
print("x.__next__() = ",x.__next__())
print("x.__next__() = ",x.__next__())

x = [1, 2, 3]
y = [4, 5, 6,7]
zipped = zip(x, y)

print("x = ",x,"y = ",y)
print("list(zipped) = ",list(zipped))
print("zipped = ",zipped)
print("list(zipped) = ",list(zipped))
#[(1, 4), (2, 5), (3, 6)]
x2, y2 = zip(*zip(x, y))
print("x2 ==" ,x2,"and","y ==", list(y2))

# x3, y3 = zipped[1]
# print("x3 ==" ,x3,"and","y3 ==", list(y3))

