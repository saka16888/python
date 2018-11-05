
arr1 = [int(tmp) for tmp in input().strip().split(' ')]
n=arr1[0]
diff=0
for i in range(n):
    arr1 = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    #print("i = ", i ," arr1 = ", arr1)
    diff += arr1[i]-arr1[n-i-1]

print(abs(diff))
