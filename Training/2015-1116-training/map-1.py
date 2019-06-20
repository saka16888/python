import math
print(math.cos(3.0))

def square(x):
    'Return a value times itself'
    return x * x

def printStar(n):
    for i in range(1,n+1):
        print("*" * i)
s = [10, 20, 30]
sq1 = []
for x in s:
    sq1.append(x ** 2)
print("sq1 =",sq1)
print("Use map function",list(map(square, s)))

s2=[2,3,4]
print(list(map(printStar,s2)))

s3=list(map(hex, s))
print("s3 = ",s3)
print(list(map(hex, s)))
