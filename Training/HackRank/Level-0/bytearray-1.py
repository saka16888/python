elements = [5, 10, 0, 0, 100]

# Create bytearray from list of integers.
values = bytearray(elements)
# Modify elements in the bytearray.
values[0] = 5
values[1] = 1
values[2:4] = [70, 89, 34]

# The array is now modified.
for v in values: print(v)
print(values)

print("*" * 40)
# Create byte from list of integers.
e2="abc"
#v1 = bytes(e2) # TypeError: string argument without an encoding
#v1=bytes(list(e2)) #TypeError: 'str' object cannot be interpreted as an integer
# v1=bytes("abc")

v1=bytes(ord(h) for h in e2)
print("v1=",v1)
v1=bytes(b"abc")
print("v1=",v1)
'''
v1=bytes(e2)
print("v1=",v1)
'''
for v in v1:
    print(v)
    print(str(v))

print("*" * 40, "bytes usage")
v2 = bytes(elements)
for v in v2:
    print(v)
print(v2)

try:
    v2[0]= 3
except TypeError as err:
    print("Error : ",err)
except:
    print("except Error ", err)
else:
    print("Else Error ",err)
finally:
    print("Final Error ")

