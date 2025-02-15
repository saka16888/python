'''
Mutable Objects (List, Dict, Set, etc.)
For mutable objects, changes inside the function persist outside
because they are passed by reference.
'''

def modify_list(lst):
    lst.append(4)  # Modifies the original list

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4] (Updated)

'''
2. Immutable Objects (Int, Str, Tuple, etc.)
For immutable objects, changes inside the function do not persist because Python passes them by value (creates a new object).

Example (Immutable - Integer)
'''

def modify_number(num):
    num += 10  # Creates a new variable, does not modify the original

my_num = 5
modify_number(my_num)
print(my_num)  # Output: 5 (Unchanged)

#Returning and Updating Immutable Objects
def modify_number(num):
    return num + 10

my_num = 5
my_num = modify_number(my_num)  # Update the original variable
print(my_num)  # Output: 15

#4. Updating Immutable Objects Inside Mutable Containers
#You can modify an immutable object if it's stored in a mutable container (like a list or dict).

def modify_element(lst):
    lst[0] += 10  # Updates the first element

my_list = [5, 2, 3]
modify_element(my_list)
print(my_list)  # Output: [15, 2, 3]


#Assignment with Mutable Objects
#With mutable objects like lists, = does not create a copy, it only assigns a reference.
a = [1, 2, 3]
b = a  # Both 'a' and 'b' point to the same list
b.append(4)
print("a b",a,b)  # Output: [1, 2, 3, 4] (changes reflect in both)

c = a.copy()  # Creates a separate copy
c.append(5)
print(a)  # [1, 2, 3, 4]
print(c)  # [1, 2, 3, 4, 5] (Only 'c' is changed)

