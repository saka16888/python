def swap(x,y):
    #x,y = y,x
    # tmp=x
    # x=y
    # y=tmp
    #print (x, y)
    return y,x


x=3; y=4
x,y = swap(x,y)
print(x,y)

def swap2(s1, s2):
    return s2, s1

# s1 = 'a'
# s2 = 'b'
s1 = ['a','b','c']
s2 = ['d','e','f']
s1, s2 = swap2(s1, s2)
print(s1,s2)