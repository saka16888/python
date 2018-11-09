from operator import itemgetter, attrgetter

def getKey(item):
    print(item)
    return item[0]
s1 = [[2, 3], [6, 7], [3, 34], [24, 64], [1, 43]]
print(sorted(s1, key=getKey))

#print(sorted(s1,key=attrgetter("v1")))
'''
'[[1, 43], [2, 3], [3, 34], [6, 7], [24, 64]]
'''
#