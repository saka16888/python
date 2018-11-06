'''""""""
    This is doc string
'''

s1=['Python','Java','C++']
for i,v in enumerate(s1):
    print(i,v)

for i,v in enumerate(s1):
    print(i,v)

'''
0 Python
1 Java
2 C++
'''

print(enumerate(s1))
print(list(enumerate(s1)))

t1=('Python','Java','C++')
print(tuple(enumerate(s1)))
print(list(enumerate(s1)))