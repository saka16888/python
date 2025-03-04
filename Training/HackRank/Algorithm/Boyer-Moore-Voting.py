'''
Given an array
nums
of
size
n,
return the
majority
element.

The
majority
element is the
element
that
appears
more
than ⌊n / 2⌋ times.You
may
assume
that
the
majority
element
always
exists in the
array.

Example
1:

Input: nums = [3, 2, 3]
Output: 3
Example
2:

Input: nums = [2, 2, 1, 1, 1, 2, 2]
Output: 2

'''

def majorityElement(nums):
    '''
    O(n) time and O(1) space
    s = list(set(nums))
    l = len(nums) / 2
    for i in s:
        c = nums.count(i)
        print(i, c, l)
        if (c := s.count(i)) > l:
            return c
    '''
    print("majorityElement",nums)
    candidate, count = None, 0
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
        print("num",num,"candidate",candidate,"count",count)
    return candidate

arr = [1, 4, 3,1, 2, 6, 5]
print("majorityElement",majorityElement(arr))
arr = [1, 4, 3,1,1,1, 2, 6, 5]
print("majorityElement",majorityElement(arr))
