'''
Shallow copy (copy(), [:], list()) → Works fine if there are no nested lists.
Deep copy (copy.deepcopy()) → Needed when lists contain nested mutable objects.
'''

# Creates a new list but only copies references for nested objects.
# Shallow copy: Changes to nested lists affect both copies.
original = [1, 2, 3, [4, 5]]
copied = original.copy()
copied[3].append(6)
copied.append(7)
print(original)  # [1, 2, 3, [4, 5, 6]]
print(copied)    # [1, 2, 3, [4, 5, 6],7]

print("Using List Slicing [:] (Shallow Copy)")
original = [1, 2, 3]
copied = original[:]
copied.append(4)

print(original)  # [1, 2, 3]
print(copied)    # [1, 2, 3, 4]

print("# Using list() Constructor (Shallow Copy)")
original = [1, 2, 3]
copied = list(original)
copied.append(4)

print(original)  # [1, 2, 3]
print(copied)    # [1, 2, 3, 4]

print("# Using copy.deepcopy() (Deep Copy)")
import copy
original = [1, 2, 3, [4, 5]]
copied = copy.deepcopy(original)
copied[3].append(6)
original.append(7)
print(original)  # [1, 2, 3, [4, 5]]
print(copied)    # [1, 2, 3, [4, 5, 6]]
# 🔹 Deep copy: Changes to nested lists do NOT affect the original.

'''
Shallow copy (copy(), [:], list()) → Works fine if there are no nested lists.
Deep copy (copy.deepcopy()) → Needed when lists contain nested mutable objects.
'''


