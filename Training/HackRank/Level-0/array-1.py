''''
Given an array like [-1, 2, 3, 5, 4, 6] and it should print   the 3 that is order of the array is equal to array element
'''

def find_index_equal_element(arr):
    for i in range(len(arr)):
        if (i == arr[i]) :
            print("arr[%d] = %d" % (i,arr[i-1]))


arr1=[-1,2,3,7,5,4,6,8,9]
find_index_equal_element(arr1)
print("arr1 = ",arr1, "\nreverse array arr1[::-1] = ",arr1[::-1])

#---------------------------------------------------------------------------------
print('*' * 40)

'''
s[i:j:k] : slice of s from i to j with step k
The slice of s from i to j is defined as the sequence of items with index k
such that i <= k < j.
If i or j is greater than len(s), use len(s).
If i is omitted or None, use 0.
If j is omitted or None, use len(s).
If i is greater than or equal to j, the slice is empty
'''

i=-1
j=5
k=-1
print("arr1[%d:%d] = %s"% (i,j,arr1[i:j]))
print("arr1[%d:%d:%d] = %s"% (i,j,k,arr1[i:j:k]))
i=1;j=4
print("arr1[%d:%d] = %s"% (i,j,arr1[i:j]))
print("arr1[:%d:%d] = %s"% (3,-1,arr1[:3:-1]))
print("arr1[:%d:%d] = %s"% (2,-1,arr1[:2:-1]))

#---------------------------------------------------------------------------------
print('*' * 40)
print("arr1=%s" % arr1)
i=1
j=i+4
arr1[i:j]=[7,8,9,10]
print("arr1[%d:%d] = %s"% (i,j,arr1[i:j]))
print("arr1=%s" % arr1)

i=2
arr1[i:i+3]=[27,28,29,20]
print("arr1[%d:] = %s"% (i,arr1[i:]))
print("arr1=%s" % arr1)

#---------------------------------------------------------------------------------

print('*' * 40)
s= list(range(1,5))
print("%s" % s)
