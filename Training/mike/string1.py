s1="this-is-string"
#s1[0]="T" # TypeError: 'str' object does not support item assignment

print(s2:=s1.join("ABC"),"\ns1",s1,"\ns2",s2)
print(s2:=s1.join(['First,',',meanwhile,',',end']),"s1=",s1,"\ns2=",s2)
#print(s2:=s1.join('First,',',meanwhile,',',end'),"s1=",s1,"\ns2=",s2)
#-------------------------------------
print("-" *50)
#-------------------------------------
# index, rindex, find, rfind, replace
# swapcase, capitalize

print("s1",s1,r's1.find("is")', s1.find("is"))
print("s1",s1,r's1.find("are")', s1.find("are"))
print(r's1.rfind("is")', s1.rfind("is"))

print(r's1.index("is")', s1.index("is"),s1.index("is",3,))
print(r's1.index("is")', s1.index("is"))
#print(r's1.index("was")', [v := s1.index("was")])
print(r's1.rindex("is")', s1.rindex("is"))
print("index : rindex: ",s1, s1.index('t'),s1.index('i'),"rindex : ",s1.rindex('i'))
print(r's1.replace("is")', s1.replace("-is",'-was',2))
print("find, return index",s1,s1.find("t",0),s1.find("is"),s1.find("-"))
print("after replace s1",s1)
print("swapcase",s1.swapcase(),s1)
print("capitalize",s1.capitalize(),s1)

#-------------------------------------
print("-" *50)
#-------------------------------------
# isupper, islower, upper,lower
# isdigit,casefold
#
print(s1,"isupper, islower",s1.isupper(),s1.islower())
print("upper", s1.upper(),"lower", s1.lower(), s1)
print("isdigit",s1.isdigit(),"isdecimal",s1.isdecimal(),"123".isdecimal())

string1 = "Straße"
string2 = "strasse"
if (s1:= string1.casefold()) == (s2 := string2.casefold()):
    print("s1", s1, "s2",s2, "The strings are equal (case-insensitive)")
print("upper", s2:=s1.upper(),"casefold",s2:=s1.casefold())

#-------------------------------------
print("-" *50)
#-------------------------------------
# count
# center
print(token:="is","count",s1.count(token))

text = "Python"
centered_text = text.center(20)
print(text,"center",f"'{centered_text}'")
#-------------------------------------
print("-" *50)
#-------------------------------------
print("join ",s1, s1.join(" that is value"))

print("concate", 3 * 'un' + 'ium')

print(s1[::-1])
reversed(s1)
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
