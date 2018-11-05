from  itertools import *
# tmp = [s for s in input().strip().split(" ")]
# n= tmp[0]
# tmp = [s for s in input().strip().split(" ")]
# s1= tmp[0]

s1="beabeefeab"

def is_alternate_string(s):
    s_len=len(s)
    print("s = ",s)
    if len(s) < 2 : return False
    if (s[0] == s[1]) : return False
    for i in range(2,s_len,2):
        if s[0] != s[i] : return False
    for i in range(3, s_len,2):
        if s[1] != s[i] : return False
    return True

def convert(s):
    if s == "":
        return 0
    s_set = set(s)
    print("s_set =",s_set)
    tmp=s
    for seq in list(permutations(s_set)):
        for c1 in seq:
            if is_alternate_string(tmp):
                print (tmp, "is_alternate_string")
                return len(tmp)
            else:
                print(tmp,"Not is_alternate_string")
                tmp=tmp.replace(c1,"")
                #print("c1 = ",c1," , tmp = ",tmp)
                convert(tmp)

# is_alternate_string("ab")
# is_alternate_string("a")
# is_alternate_string("aa")
# is_alternate_string("aba")
print(convert(s1))
