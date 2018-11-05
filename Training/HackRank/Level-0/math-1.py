import math
print(math.cos(3.0))

def square(x):
    'Return a value times itself'
    return x * x

s = [10, 20, 30]
squares = []
for x in s:
    squares.append(x ** 2)
print(squares)
print(list(map(square, s)))
print(list(map(hex, s)))
