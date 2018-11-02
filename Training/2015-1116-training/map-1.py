import math
print(math.cos(3.0))

def square(x):
    'Return a value times itself'
    return x * x

def printStar(n):
    for i in range(1,n+1):
        print("*" * i)
s = [10, 20, 30]
squares = []
for x in s:
    squares.append(x ** 2)
print(squares)
print(list(map(square, s)))

s2=[2,3,4]
print(list(map(printStar,s2)))

print(list(map(hex, s)))
