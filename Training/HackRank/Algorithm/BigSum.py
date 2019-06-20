'''
tmp = [int(arr_temp) for arr_temp in input().strip().split(' ')]
n=tmp[0]
'''
#arr1 = [float(arr_temp) for arr_temp in input().strip().split(' ')]
arr1=[1.2, 3.4, 5.6]
sum=0
for v in arr1:
    print("%20r" % v)
    sum += v
print("%10f" % sum)
print("%10f" % sum(arr1))