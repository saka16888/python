
a=26.333
print(int(a))
print(str(a))
try:
    print(int(int(a),8))
except:
    print("fail to convert int(int(a),8)")

a='26.588'
# Error  found: int(a)
print(int(float(a)),float(a))

x=23
print(bin(x),oct(x),hex(x))
oct_x=oct(x)
print("oct",int(oct_x,8))

hex_x=hex(x)
print("hex ",hex_x,int(hex_x,16))