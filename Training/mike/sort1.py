a1=[1,3,5]
b1=[1,6,7]


c1=sorted(a1+b1)
print(c1)

s1="abc"
s2="asdef"

s3=sorted(s1+s2)
print(s3,"".join(s3))

#convert array to string
sorted("This is a test string from Andrew".split(), key=str.casefold)
#['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']


student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

print(student_tuples)

print(sorted(student_tuples, key=lambda student: student[2]))   # sort by age
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

print(student_tuples)

'''
Both list.sort() and sorted() accept a reverse parameter with a boolean value.
This is used to flag descending sorts.
For example, to get the student data in reverse age order:
'''
from functools import partial
from unicodedata import normalize

names = 'Zoë Åbjørn Núñez Élana Zeke Abe Nubia Eloise'.split()

print(sorted(names, key=partial(normalize, 'NFD')))
#['Abe', 'Åbjørn', 'Eloise', 'Élana', 'Nubia', 'Núñez', 'Zeke', 'Zoë']

print(sorted(names, key=partial(normalize, 'NFC')))
#['Abe', 'Eloise', 'Nubia', 'Núñez', 'Zeke', 'Zoë', 'Åbjørn', 'Élana']

a=-3.3
b=3
print(a//b, a/b, a%b)
