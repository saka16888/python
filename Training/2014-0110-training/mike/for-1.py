a = [1, 2, 3, 4, 5]
b = [100, 200, 300, 400, 500]

print(b)
for idx, value in enumerate(a):
    b[idx] += value

print(a)
print(b)

x=0
y=1
sum = lambda x,y: x+y
print("%d" % sum(x,y))
print(True if x==y else False)
