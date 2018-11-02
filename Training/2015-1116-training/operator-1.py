
x,y =12, 7
def op(x,operator,y):
    print("%d%s%d" % (x,operator,y))
    tmp="".format("%d%s%d" % (x,operator,y))
    print(tmp," = ",tmp)

print("%d %s %d = %d" % (x,'+',y,x+y))
print("%d %s %d = %d" % (x,r'+',y,x+y))
print("%d %s %d = %d" % (x,'%',y,x%y))
print("%d %s %d = %d" % (x,'/',y,x/y))
print("%d %s %d = %r" % (x,'/',y,x/y))
z=x//y
print("%d %s %d = %r" % (x,'//',y,z))

print("%d %s %d = %r" % (x,'divmod',y,divmod(x,y)))
x,y =-12, 7
print("%d %s %d = %r" % (x,'divmod',y,divmod(x,y)))
"bitwise operations"
print("%d %s %d = %r" % (x,'//',y,z))

