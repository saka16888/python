import re

# def reduce_string(s):
#     print("s = ", s)
#     s_len=len(s)
#     for i in range(s_len-1):
#         print(i,"len = ",s_len)
#         if ( s[i] == s[i+1]) :
#             s=s.replace(s[i:i+2],"",-1)
#             print("modify s = ",s)
#             s=reduce_string(s)
#     return(s)

if __name__ == '__main__':

    s="aaabccaaddd"
    #s = "aa"
    # print("%s, %s" % (s,s[0:2]))
    # s=s.replace(s[0:2],"",-1)
    # print("s = ",s)
    # s=reduce_string(s)
    # if s != "" :
    #     print(s)
    # else:
    #     print("Empty String")

    #regex = re.compile(r'(\w)(\1)')
    #match = regex.search(s)
    pattern=r'(\w)(\1)'
    match = re.search(pattern,s)
    while match:
        print("s = ",s," match.group()",match.group())
        s = s.replace(match.group(),'')
        match = re.search(pattern,s)
    print(s) if s else print('Empty String')
