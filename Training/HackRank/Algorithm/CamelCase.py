import re

#list1 = [tmp for tmp in input().strip().split(" ")]
#s=list1[0]
s="saveChangesInTheEditor"
# if s[0].isupper() :
#     print("Upper", s)
# else:
#     print("Lower ", s)

def word_count(s):
    # r1 = re.compile(r'[A-Z]')
    # print(r1.findall(s))
    # #  The two lines is equal this line
    nlist = re.findall(r'[A-Z]',s)
    print("nlist = ", nlist, " ", len(nlist), "count = ", nlist.count('Z'))
    if s[0].isupper():
        return len(nlist)
    else:
        return len(nlist)+1

if __name__ =='__main__':
    print(word_count(s))
