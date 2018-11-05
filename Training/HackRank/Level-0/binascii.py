import binascii

'''
from bitstring import BitArray

a = BitArray(bin='11101011')
b = BitArray(bin='10001001')
c = a^b
print("%d  %d  %b" % (a,b,c))

'11111111'.fromBinaryToInt()
int('11111111', 2)
'''

d = ['Spring', 'Summer', 'Fall', 'Winter']
for i, j in enumerate(d,1):
    print(i, j)
print("\n","a","b")
print("\n%s%s"%("a","b"))
for i, j in enumerate(d, 0):
    print(i, j)

crc = binascii.crc32(b"hello")

print('crc32 = {:#010x}'.format(crc))
crc = binascii.crc32(b"32", crc) & 0xffffffff
print('crc32 = {:#010x}'.format(crc))