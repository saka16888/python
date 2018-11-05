#!/bin/python3
import re
import sys

# l1 = [int(tmp) for tmp in input().strip().split(" ")]
l1=[5]
a1 =l1[0]
# a2 = [int(tmp) for tmp in input().strip().split(" ")]
a2=[2,4,5,67]
print("Sum of a2 ",a2, " = ", sum(a2))

x=25
y= float(x)
print(y)
print('y = %s, %d' % (y, y))

ip_addr="191.2.3.4 "
aa=re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",ip_addr)
print("aa=",aa)

print(str('hi'))
print(repr('hi'))
print('%d , %s, %r' % (1,'1','1'))
#exit()

'''
n = int(input("Enter number list").strip())
print('total number = ',n)
'''
#print("Enter number list")

tmp=input("Enter number list : ").strip().split(' ')
print("tmp = ",tmp)

arr = [int(arr_temp) for arr_temp in tmp]
print("arr = ",arr)
sum = 0
for i in arr :
    sum = sum + i
print('\nsum of arr ',arr,'=', sum, '\nsort arr', sorted(arr))

str1=str(tmp)
print('str1 = %s' % str1)

reverse_arr=reversed(arr)
print('reverse_arr = ',list(reversed(arr[1:2])))
reversed_arr2 = arr[::-1]
print('reversed_arr2 = ',reversed_arr2)


print(list(filter(lambda x: x % 2 == 0, arr)))

