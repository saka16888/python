dict = {
    'item1': 1,
    'item2': 2,
}

d2_data = {
    'item3': 3,
    'item2': 2,
}

print(dict)
dict['item3'] = 3
print(dict)
dict.update({'item4': 5})
print(dict)
dict.update({'item4': 4})
print(dict)

# TypeError: unsupported operand type(s) for +=: 'dict' and 'dict'
# dict += {'item5': 5}
# d4 is the reference of dict
dict4=dict
dict['item3'] = 31
print("dict  =",dict)
print("dict4 =",dict4)

dict['item6'] = 6
print(dict)
key='item10'
if key in dict :
    print(dict[key])
else:
    print(key," is not in",dict)

# duplitcate key, the last assignment wins
# dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
# print("dict['Name']: ", dict['Name'])

# len
print(dict,"len =",len(dict))

# items
print("Value : %s" %  dict.items())

dict3 = dict.copy()
print("New Dictinary : %s" %  dict3)
dict['item7'] = 7
print("dict  = ",dict)
print("dict3 = ",dict3)

del dict['item6']; # remove entry with key 'Name'
print(dict)
dict.clear();     # remove all entries in dict
print(dict)
del dict
# print(dict)

'''
The Python 2 builtin cmp() has been removed in Python 3.0.1,
although it remained in Python 3.0 by mistake. It is mostly used when defining the __cmp__ comparison method or functions to pass as cmp parameters to .sort() and
the support for this has been removed in Python 3 as well.
print(dict,"cmp ",d2_data, cmp(dict,d2_data))
'''
