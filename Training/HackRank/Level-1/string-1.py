
# replace
s1="this is string example....wow!!! this is really string"
print(s1)
print(s1.replace("is", "was"))
s1="this is string example....wow!!! this is really string"
print(s1.replace("is", "was", 3)) ; # replace max 3  times
print(s1.replace("is", ""))

#
# convert t string
tmp=["3","6","9","a"].remove("a")
print("tmp = ", tmp)
t="12"
#str2 = (str(t+c) if c.isalpha() else c.upper() for c in tmp )
#print('str2 = ', list(str2))

tmp="3869abc"
print('tmp=',tmp,'\nlist(tmp)=',list(tmp),'\nsorted(tmp) =',sorted(tmp))
t=""
str2 = [str(t+c) if c.isnumeric() else c.upper() for c in tmp]
print('str2 = ', str2)

c1="Hello"
print("c1 Join = ",c1.join("Everyone168"))
str2 = [c1.join(c) if c.isnumeric() else c.upper() for c in tmp]
print('str2 = ', str2)

str2 = [[ord(c),c] for c in tmp]
print('str2 = ', str2)