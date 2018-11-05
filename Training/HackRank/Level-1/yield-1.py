def g(x,y):
    yield from range(x, y, -1)
    #yield from range(x)

print(g(5,1))
print(list(g(5,1)))

print(list(g(6,3)))