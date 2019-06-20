import sys

# n=int(input().strip())
# k=int(input().strip())
n=150
k=100

def adjSwap(n):
    tmp=0
    for i in range(n):
        for j in range(i+1,n):
            tmp += 1
    tmp %= 1000000007
    return tmp

def Swap(n,k):
    if k>n : k=n
    tmp=1
    for i in range(1,k+2):
        # print(i)
        tmp *= i
    tmp %= 1000000007
    return tmp

print(adjSwap(n))
print(Swap(n,k))