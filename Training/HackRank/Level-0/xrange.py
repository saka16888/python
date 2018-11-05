count = 0
for n in range(10):
    print("n = %d" % n)
    count += n
print(count)

'''
range in Python 3.x is
xrange from Python 2.x.
It was in fact Python 2.x's range that was removed
'''
# count = 0
# for n in xrange(100):
#     count += n
# print(count)