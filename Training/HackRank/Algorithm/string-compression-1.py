import os

s1= "aabbggeeeecaaddd"
s1_len = len(s1)
tmp = s1 + str(s1_len)
print(tmp)

def compress(str1):
    tmp=""
    str_len = len(str1)
    i = 0
    while ( i <= str_len-1 ):
            j = i
            #print("j  = ",j)
            tmp += str1[j]
            count = 1
            while i < str_len-1:
                if (str1[j] == str1[i+1]):
                    #print("i  = ", i)
                    count += 1
                    i += 1
                else:
                    break
            i += 1
            tmp += str(count)
    return tmp

print(compress(s1))