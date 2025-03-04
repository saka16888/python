'''
Use append() when you want to add a single element (including another list as a sublist).
Use extend() when you want to merge two lists or add multiple elements at once.
'''

def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    print("nums", nums, "val", val)
    r1=[i for i in nums if i!= val]
    '''
    for i in nums:
        print("i",i)
        if val != i:
            r1.append(i)
    '''
    nums.clear()
    nums.extend(r1)
    print("r1", r1)
    return len(r1)

def removeElement2(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    print("nums", nums, "val", val)
    l=len(nums)
    i=0
    for i in nums:
        print("i", i)
        if i == val:
            nums.remove(i)
    print("nums",nums)
    return len(nums)

nums=[3,2,2,3]
val=3
print(removeElement(nums,val))
nums=[0,1,2,2,3,0,4,2]
val=2
print("print(removeElement(nums,val))",removeElement(nums,val))

nums=[0,1,2,2,3,0,4,2]
val=2
print("removeElement2(nums,val))",removeElement2(nums,val))


a1=[13,-1,22,33]
print("index", a1.index(22), a1.index(13))
a1.insert(1,14)
print(a1)
print(enumerate(a1))

for i, e in enumerate(a1):
    print(i,e)

s1="abcdef"
for i, e in enumerate(s1):
    print(i,e)

a1.reverse()
print(a1,a1.index(-1),a1.index(33))

t=a1.pop()
print(f"After popping element: {t}")

print("a1",a1)
t=a1.pop(2)
print("a1.pop(2)",a1.pop(2),t)
print("a1",a1)

for i in range(len(a1)):
    print(i,a1[i])

s1="abc["
print("s1 min",min(s1),"max",max(s1))

numbers = [1, 5, 2, 82, 3]
min_number = min(numbers)
max_number = max(numbers)
print(f"Minimum: {min_number}")
print(f"Maximum: {max_number}")

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in numbers if num % 2 == 0]
print(f"Even numbers: {even_numbers}")

arr = [1, 4, 3, 2, 6, 5]
print("arr2", arr2:=arr[:]+[123])
print("reversed and array.reversed", reversed(arr),arr,arr2.reverse(),arr2)
reversed_arr = list(reversed(arr))
print(reversed_arr,arr)  # Output: [5, 6, 2, 3, 4, 1]

arr = [1, 4, 3, 2, 6, 5]
index=1
print("arr.pop()","index",index,"value",arr.pop(index))
print("arr after pop 1",arr)


