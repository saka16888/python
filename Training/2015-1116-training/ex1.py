# hot-key
# Ctrl-pre ctrl-next 
# atl-prev | alt-next
''' hello '''

print(-2%5)
x=10
hex(id(x))
print("id x = %r, %r" % (hex(id(x)), id(x)) )
print(format("hello %s" % "world"))
y=5+5

def printstart(n,d):
    for i in range(1,n+1):
        j=i%d
        if j != 0: print("*" * (i % 6))

printstart(10,6)

s1="\r\nfgeg\r\ndfbeb"
print(s1.strip())

for i in range(5) :
    print(i)
    print(i)
print('Howdy!')

n = 8

for i in range(n):
    pad = ' ' * i
    print(pad, 'Welcome to Python World!')
    s1 = r"int 0/" + str(i) + chr(13)
    #s1 = r"int 0/" + chr(13)
    r1 = r"(Interface 0/" + str(i) + ")#"
    print(s1,r1)

print(i ** 2)

print('Howdy!')

n = 8

for i in range(n):
    pad = ' ' * i
    print(pad, 'Welcome to Python World!')

print(i ** 2)

import os
print(os.getcwd())
print(os.chdir("."))

print("__name__ =",__name__)
if __name__ == '__main__':
    print("hello")