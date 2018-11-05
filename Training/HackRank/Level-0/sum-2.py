import os
import sys

def sum(numbers):
    tmp = 0
    for n in numbers:
        tmp += int(n)
    return tmp

#num1 = int(input())
#nums = input().strip().split(" ")
num1 = 5
nums = [1,3,4,2,5]
print(sum(nums))
