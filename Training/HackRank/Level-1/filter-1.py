arr=[21,1,1,3,4,5,4,7,11,5,5,11]

tmp = 0

for i in set(arr):
    count = arr.count(i)
    if count > 1:
        print(i,count)

def odd(n):
    return (True if n%2 == 1 else False)
print(list(filter(lambda x: x % 2 == 1, arr)))

print(list(filter(odd, arr)))

x=2
print(x**2)