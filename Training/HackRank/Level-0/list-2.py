# n = int (input ())
# s = [int (i) for i in input ().strip ().split ()]
s=[2,3,1]
print(s)
s_len=len(s)
for j in s:
    try:
        print(j,s[(j-1)%s_len])
    except IndexError as msg:
        print(j)