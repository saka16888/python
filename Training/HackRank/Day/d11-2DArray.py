#!/bin/python3

import sys

# arr = []
# for arr_i in range(6):
#    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
#    arr.append(arr_t)
arr=[
[1,1,1,0,0,0],
[0,1,0,0,0,0],
[1,1,1,0,0,0],
[0,0,2,4,4,0],
[0,0,0,2,0,0],
[0,0,1,2,4,0]]
n=6
list_sum=[]
for i in range(n-2):
    for j in range(n-2):
        tmp = (arr[i][j] + arr[i][j+1] + arr[i][j+2] +
            arr[i+1][j+1] +
            arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
        #print("sum[%d][%d] = %d" % (i,j,tmp))
        list_sum.append(tmp)

print(max(list_sum))
