
arr1 = [int(tmp) for tmp in input().strip().split(' ')]
arr2 = [int(tmp) for tmp in input().strip().split(' ')]

print(zip(arr1,arr2))
print(list(zip(arr1,arr2)))
a1_score = len([1 for a,b in zip(arr1,arr2) if a>b])
a2_score = len([1 for a,b in zip(arr1,arr2) if a<b])
print(a1_score, a2_score)
