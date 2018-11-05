from itertools import *

s1=[1,2,3]
s2=[4,5,6]
s3=['a','b','c']

'''
Also note that ifilter became filter in Python-3
(hence removed from itertools).
'''
print(list(filter(lambda x: x%2, range(10))))

func=chain
print(func ,list(func(s1,s2)))
func=product
print(func ,list(func(s1,s2)))
print(func ,list(func(s1,s2,s3)))

func=permutations
print(func ,list(func(s3)))
print(func ,list(func(s3,2)))
print(func ,list(func(s3,1)))

func=combinations
print(func ,list(func(s3,3)))
print(func ,list(func(s3,2)))
print(func ,list(func(s3,1)))

