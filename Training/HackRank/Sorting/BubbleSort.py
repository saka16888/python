# def bubble(List):
#     for j in range(len(List)-1,0,-1):
#         for i in range(0, j):
#             if List[i] > List[i+1]:
#                 List[i], List[i+1] = List[i+1], List[i]
#     return List

# n = int (input ().strip ())
# a = [int (i) for i in input ().strip ().split (' ')]
n=6
a=[3,2,6,1,7,9]
print ('a = %s' % a)
numberOfSwaps = 0
for i in range (n-1,0,-1):
    for j in range (i):
        # Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]):
            # tmp = a[j]
            # a[j] = a[j + 1]
            # a[j + 1] = tmp
            a[j], a[j + 1] = a[j+1], a[j]
            numberOfSwaps += 1

print ('Array is sorted in %d swaps.' % numberOfSwaps)
print ('First Element: %d' % a[0])
print ('Last Element: %d' % a[n - 1])
print ('a = %s' % a)