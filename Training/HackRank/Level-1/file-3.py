import re

filename = '../notes/team.txt'
try:
    with open(filename,mode='r') as f:
        buf = f.read()
        '''
                for line in f:
                    print(line,end="")
            '''

    print("buf =",buf)
    print(filename,"is closed :", f.closed)
except:
    print("Error : fail to open file",filename)

print(filename,"is closed :",f.closed)
if (f.closed):
    f.close()
    print("close ",filename)

'''
buf="this is my file \
eygevehb \
eyffvehb"
'''

ret=re.findall(r'e[ay]*vehb',buf)
print("ret=",ret)
ret=re.findall(r'ey([ge|ff]*)vehb',buf)
print("ret=",ret)

pat=re.compile(r'ey([ge|ff]*)vehb')
r2=pat.search(buf)
if r2:
    print("r2.group(0)=",r2.group(0))
    print("r2.group(1)=",r2.group(1))
    #print("r2.group(2)=",r2.group(2))
else:
    print("r2 =",None)

ret=re.findall(r'ey(\w*)vehb',buf)
print("ret=",ret)
ret=re.findall(r'ey*vehb',buf)
print("ret=",ret)
ret=re.findall(r'ey(.*)vehb',buf)
print("ret=",ret)
