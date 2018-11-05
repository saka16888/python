def sq(x): return x*x
print(map(sq, range(1, 11)))
print(list(map(sq, range(1, 11))))

def double(x): return x+x
print(list(map(double,"abcd")))

def add(x, y): return x+y
print(list(map(add, range(8), range(8))))
print(list(map(add, range(8), range(9))))

x1=[1,3,5,7,9]
y1=[2,4,6,8]
print(list(map(add,x1,y1)))
