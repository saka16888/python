import os
'''
def isprime(n):
    if n < 2:
        return False
    if ( (n == 2) | (n == 3)) :
        return True
    if n % 2 == 0:
        return False
    max = n**0.5+1
    i = 3
    while i <= max:
        if n % i == 0:
            return False
        i+=2
        return True
'''

def isprime(n):
    if n == 2: return True

    # 0 and 1 are not primes
    if n < 2:
        return False

    # 2 is the only even prime number
    if n == 2:
        return True

    # all other even numbers are not primes
    if not n & 1:
        return False

    # range starts with 3 and only needs to go up
    # the square root of n for all odd numbers
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True

def primes(arr):
    # Fill in code
    # tmp=[]
    # for x in arr :
    #     if isprime(x):
    #         tmp.append(x)
    #     else:
    #         pass
    return [x for x in arr if isprime(x)]
    #return [x if isprime(x) else (x**2+1) for x in arr]

# arr1=[2,3,4,5,6,7,9,11,12,13,17,14,16,19,21,23,2526,27,29,31,35,37,41,43]
#print(enumerate(primes(arr1))
arr1=range(2,100)
print(primes(arr1))
for i, p in enumerate(primes(arr1)) :
    print(i,p)
    #print(p)
    if i > 10:
        break

m=4
m &= 2
print(m)
