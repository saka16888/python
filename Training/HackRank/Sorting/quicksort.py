from random import *

def quick_sort(lst):
    if len(lst) == 1:
        return lst

    for i in range(1, len(lst)):
        temp = lst[i]
        #print("i = %d, temp = %d, lst = %r" %(i,temp,lst))
        j = i - 1
        while j >= 0 and temp < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
            #print(lst)
        lst[j + 1] = temp
    return lst

def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        return qsort([x for x in arr[1:] if x < arr[0]]) + [arr[0]] + qsort([x for x in arr[1:] if x >= arr[0]])

a= [randint(1,100000) for i in range(1000)]
#a=[7,5,6,33,45,23,67,3,2,1,12,34,654,3,56,34,22,893,126]
print(a)
print("quick_sort  =",quick_sort(a))
#print("qsort          =",qsort(a))
