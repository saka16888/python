list1 = ['1', '2', '3']
s1 = ''.join(list1)
print(s1)

list1 = [4, 2, 3]
s1 = ''.join(str(e) for e in list1)
print(s1)

a1 = {5, 7, 3}
s2 = ''.join(str(e)+" " for e in a1)
print("s2 =", s2)

s2 = ''.join(str(e) for e in a1)
print("s2 =",s2)

print(s1.ljust(5, "h"))
print("s1 =", s1)

