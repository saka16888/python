from functools import reduce
import sys, operator

print(sum([1,2,3,4]))
print(reduce(lambda x, y: x+y, [1, 2, 3, 4]))
print(reduce(operator.add, [1,2,3,4],0))
print(reduce(operator.xor, [1,2,3,4],0))
#10

#num1 = int(input())
#s = input('Enter a line ("q" to quit):')
#print(s)
#nums = input().strip().split(" ")
#print(nums)

#print(reduce(lambda x, y : x^y, map(lambda x : int(x), list(nums))))

nums = [1,2,3,4,3]
f1=lambda x,y: x^y
print(reduce(f1, map(lambda x : int(x), list(nums))))
print(reduce(f1, list(nums)))

#reduce(operator.xor, list(nums))
print(reduce(operator.xor, map(lambda x : int(x), list(nums))))

nums=[7,1,21,3,1,2,4,3,4,2,7]
print(reduce(operator.xor, map(lambda x : int(x), list(nums))))
print(reduce(operator.xor, list(nums)))

#nums.reduce(:^)
