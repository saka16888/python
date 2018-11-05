import sys


# n = int(input().strip())
# arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

arr = [1,3,6,7]
tmp=''
for i in arr[::-1]:
    tmp += str(i) + '  '
print(tmp)

