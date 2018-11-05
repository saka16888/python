from functools import reduce

class Vector:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector (self.a + other.a, self.b + other.b)

v0 = Vector()
v1 = Vector (2, 10)
v2 = Vector (5, -2)
v3 = Vector (7, 9)
print(v0)
print(v1)
print(v1 + v2)
vlist=[v0,v1,v2,v3]

print(reduce(lambda x,y: x+y,vlist))
print(reduce(lambda x,y: x+y,vlist))