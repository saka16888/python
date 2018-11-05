xvec = [10, 20, 30,40]
yvec = [2, 5, 3]
#tmp += xvec
#print(tmp)
#ret = sum(tmp += x for x in xvec)
print(xvec,yvec,zip(xvec, yvec),list(zip(xvec, yvec)))
ret = sum(x * y for x, y in zip(xvec, yvec))
print("ret = %d" % ret)

ret = sum(x ^ y for x, y in zip(xvec, yvec))
print("ret = %d" % ret)

zipped = zip(xvec,yvec)
print(xvec, yvec, list(zipped))

ret = sum(x ** y for x, y in zip(xvec,yvec))
print("ret = %d" % ret)
