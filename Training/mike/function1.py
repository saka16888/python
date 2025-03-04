def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

i = 5
def f2(arg=i):
    print(arg)

i = 6
f2()