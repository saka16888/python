s1="this-is-a-string"
#s1[0]="T" # TypeError: 'str' object does not support item assignment

print("index : rindex: ",s1, s1.index('t'),s1.index('i'),"rindex : ",s1.rindex('i'))

print("isupper, islower",s1.isupper(),s1.islower())
print("upper", s1.upper(),"lower", s1.lower(), s1)

print("replace", s1.replace("t", "i"))
print("swapcase",s1.swapcase())
print("isdigit",s1.isdigit())

print("find, return index",s1,s1.find("t",0),s1.find("is"),s1.find("-"))

print("join ",s1, s1.join(" that is value"))

print("concate", 3 * 'un' + 'ium')

print(s1[::-1])

print(s1.swapcase())
print(s1)
print(s1[::2])
print("s1[2:7:2]",s1[2:7:]) # 7 is end index exclusive


t1=s1.replace("t", "o")
print("replace", s1,t1)

def is_palindrome(s):
    return s == s[::-1]

def is_palin(s):
    return s == s[::-1]

print(is_palindrome(s1))
s2="sdvdsv"
print(is_palin(s2))

def longest_common_substring(s1, s2):
    m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]
    # print("m=",m)
    longest, x_longest = 0, 0
    for x in range(1, 1 + len(s1)):
        for y in range(1, 1 + len(s2)):
            print("s1[", x - 1, "]=", s1[x - 1], "s2[", y - 1, "]=", s2[y - 1])
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0
            print("m[",x,"][",y,"]", m[x][y])
        print(m)
    return s1[x_longest - longest: x_longest]

print(longest_common_substring("abc","dabch"))
#print(longest_common_substring("wdabvabc","abveabcvabcc"))
