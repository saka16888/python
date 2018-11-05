import os

def kth_element(arr1, arr2, k):
    if len(arr1) == 0:
        if (k < len(arr2)):
            return arr2[k]
        else:
            return ""
    elif len(arr2) == 0:
        if (k < len(arr1)):
            return arr1[k]
        else:
            return ""

    mida1 = int(len(arr1)/2)
    mida2 = int(len(arr2)/2)
    if (mida1+mida2<k):
        if arr1[mida1]>arr2[mida2]:
            return kth_element(arr1, arr2[mida2+1:], k-mida2-1)
        else:
            return kth_element(arr1[mida1+1:], arr2, k-mida1-1)
    else:
        if arr1[mida1]>arr2[mida2]:
            return kth_element(arr1[:mida1], arr2, k)
        else:
            return kth_element(arr1, arr2[:mida2], k)

a=[2,4,5,9,12,23,24,26,28,33,36,48]
b=[3,6,5,8,9,11,14,15,17]
k=12
sum=sorted(a+b)
if k < len(sum):
    print('kth element %s' % sum[k])

print('kth element = %s' % kth_element(a,b,k))
