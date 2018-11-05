from itertools import combinations

# tmp=[i for i in input().strip().split()]
# S=tmp[0]
# k=int(tmp[1])

def allcombination(s,k):
    upper_set=sorted([m for m in s if m.isupper()])
    print("upper_set",upper_set)
    all=[]
    for i in range(k):
        tmp=list(combinations(upper_set,i+1))
        print("tmp",tmp)
        t =["".join(e) for e in tmp]
        all.extend(t)
    for j in all:
        print(j)

S="SENDING"
k=10
allcombination(S,k)
