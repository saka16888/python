
def modify(s):
    return(s.replace("he"," Modified "))
    #s="modify"

s1= "hello"
print("s1 = ",s1)
s3=modify(s1)
print("after modify(s),  s1= ",s1, " s3 = ",s3)
s2 = s1.replace("o","")
print("after s1.replace,  s1= ",s1, " s2 = ", s2)

#----------------------------------------------------------------------
# var assignment
a = [1, 2, 3]
b = a
b.append(4)
b = ['a', 'b']
print(a, b)

d=[1,2,3,5]
c = [1, 2, 3]
d = c
d.append(4)
d = ['c', 'd']
print(c, d)

#----------------------------------------------------------------------
def foo(a):
    print(id(a))
    a.append(1)

a = []
print(id(a))
foo(a)
print(a)

#----------------------------------------------------------------------
'''
The parameter passed in is actually a reference to an object,
but the reference is passed by value.
'''
def foo1(a):
    print('In fool, a id',id(a))
    a.append(1)
    # re-assignment
    a = [1, 2]

a = []
print('In fool, a id',id(a))
foo1(a)
print(a)

#----------------------------------------------------------------------
def try_to_change_list_reference1(the_list):
    print('got', the_list)
    the_list = ['and', 'we', 'can', 'not', 'lie']
    print('set to', the_list)

outer_list = ['we', 'like', 'proper', 'English']

print('\nbefore, outer_list =', outer_list)
try_to_change_list_reference1(outer_list)
print('after, outer_list =', outer_list)

#----------------------------------------------------------------------
def try_to_change_string_reference2(the_string):
    print('got', the_string)
    the_string = 'In a kingdom by the sea'
    print('set to', the_string)

outer_string = 'It was many and many a year ago'

print('\nbefore, outer_string =', outer_string)
try_to_change_string_reference2(outer_string)
print('after, outer_string =', outer_string)

#----------------------------------------------------------------------
