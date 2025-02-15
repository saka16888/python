'''
Use append() when you want to add a single element (including another list as a sublist).
Use extend() when you want to merge two lists or add multiple elements at once.
'''




a1=[13,-1,22,33]
print("index", a1.index(21), a1.index([13]))

a1.insert(1,14)
print(a1)
print(enumerate(a1))

for i, e in enumerate(a1):
    print(i,e)

a1.reverse()
print(a1,a1.index(-1),a1.index(33))

t=a1.pop()
print(f"After popping element: {t}")

for i in range(len(a1)):
    print(i,a1[i])


numbers = [1, 5, 2, 82, 3]
min_number = min(numbers)
max_number = max(numbers)
print(f"Minimum: {min_number}")
print(f"Maximum: {max_number}")

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in numbers if num % 2 == 0]
print(f"Even numbers: {even_numbers}")

arr = [1, 4, 3, 2, 6, 5]
print(reversed(arr),arr.reverse())
reversed_arr = list(reversed(arr))
print(reversed_arr)  # Output: [5, 6, 2, 3, 4, 1]
