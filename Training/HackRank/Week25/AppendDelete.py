
s="hackerhappy"
t="hackerrack"
k=9
s="apple"
t="apple"
k=5

s="abcd"
t="abcef"
k=4

# s="abcd"
# t="abcef"
# k=5

def verifyAppDel(s,t,k):
    s1,t1=len(s),len(t)
    if (k>=(s1+t1)):
        print ("Yes")
        return
    loc=min(s1,t1)
    for i in range(min(s1,t1)):
        if s[i] != t[i]:
            loc=i
            break
    step=s1-loc+t1-loc
    print (loc,step)
    if (step == 0):
        if (k % 2 == 1):
            print ("No")
        elif (step <= k) :
            print("Yes")
        else:
            print ("No")

verifyAppDel(s,t,k)
