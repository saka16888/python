def solution(nums):
    print("nums =",nums)
    tmp=[]
    for i in nums:
        print("i =",i)
        if i == 0:
            nums.remove(i)
            nums.append(0)
            print("loop", nums)
    #nums.extend(tmp)
    print("result nums =", nums)
    return nums

def move_zeros(arr):
    n = len(arr)
    non_zero_index = 0  # Pointer to place the next non-zero element

    # Shift non-zero elements to the front
    for i in range(n):
        if arr[i] != 0:
            arr[non_zero_index] = arr[i]
            non_zero_index += 1
            #print("loop", nums)

    # Fill the rest with zeros
    for i in range(non_zero_index, n):
        arr[i] = 0

    return arr
'''
nums=[0,1,0]
print(solution(nums))
nums=[0, 0, 29, 0, 0, 1, 59, 45]
print(solution(nums))
'''

nums=[0]
print("move_zeros",move_zeros(nums))

nums=[1]
print("move_zeros",move_zeros(nums))

nums=[0, 0, 29, 0, 0, 1, 59, 45]
print(move_zeros(nums))
