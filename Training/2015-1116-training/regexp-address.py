import re

with open('notes/team_history.txt') as f:
    hist = f.read()
print(hist,"\n")

#----------------------------------------------------------------------------------------------------------
print("#" * 30,"-------------- Mac address--------------", "#" * 30)

pattern='[0-9A-F]{2}'
ret=re.findall(pattern,hist,re.I)
print("pattern = %s  ,\nret = %s" % (pattern, ret))

pattern='([0-9A-F]{2}[:.-])'
ret=re.findall(pattern,hist,re.I)
print("pattern = %s  ,\nret = %s" % (pattern, ret))

pattern='[0-9A-F]{2}[:.-]'
ret=re.findall(pattern,hist,re.I)
print("pattern = %s  ,\nret = %s" % (pattern, ret))

pattern=r'[0-9a-f]{2}[:.-]'
ret=re.findall(pattern,hist,re.I)
print("pattern = %s  ,\nret = %s" % (pattern, ret))

pattern='([0-9A-F]{2}[:.-]){5}'
ret=re.findall(pattern,hist,re.I)
print("pattern = %s  ,\nret = %s" % (pattern, ret))

pattern='(([0-9A-F]{2}[:.-]){5})'
ret=re.findall(pattern,hist,re.I)
print("pattern = %s  ,\nret = %s" % (pattern, ret))

print("#" * 30,"-------------- findall   re.DEBUG --------------", "#" * 30)
pattern=r'([0-9a-fA-F]{2}[:.-]){5}([0-9a-fA-F]{2})'
ret=re.findall(pattern,hist,re.I and re.DEBUG)
print("pattern = %s  ,\nret = %s" % (pattern, ret))

pattern=r'((([0-9a-fA-F]{2})[:.-]){5}([0-9a-fA-F]{2}))'
ret=re.findall(pattern,hist,re.I)
print("pattern = %s  ,\nret = %s" % (pattern, ret))

pattern=r'((([0-9a-fA-F]{2})[:.-]){5})([0-9a-fA-F]{2})'
ret=re.findall(pattern,hist,re.I)
print("pattern = %s  ,\nret = %s" % (pattern, ret))

pattern=r'(((([0-9a-fA-F]{2})[:.-]){5})([0-9a-fA-F]{2}))'
ret=re.findall(pattern,hist,re.I)
print("pattern = %s  ,\nret = %s" % (pattern, ret))

pattern=r'([0-9A-F]{2}[:-]){2}([0-9A-F]{2})'
ret = re.findall(pattern, hist, re.I)
print("pattern = %s  ,\nret = %s" % (pattern, ret))
# if ret:
#     print("ret = ",ret)
#     #print(ret.group(0))

print("#" * 30,"\n-------------- Not a good script, it will fail once it can't find the pattern --------------", "#" * 30)
# Not a good script, it will fail once it can't find the pattern
ret = re.search(r'([0-9A-F]{2}[:-]){5}([0-9A-F]{2})', hist, re.I)
if ret:
    print("ret.group = ",ret.group())
    print(ret.group(0)) ; # error
    print(str(ret.group(0)).replace(":",""))
    mac=str(ret.group(0)).replace(":","")
    print("mac = ",mac)
    x = int(mac,16)
    print("x = %x" % x)
#
ret = re.search(r'(00[:-]a0[:-]c9)', hist, re.I)
if ret:
    print("ret groups = ",ret.group())
else:
    assert ret is None, "MAC address is not configured"

#-------------------------------------------------------------------------
print("*************** findall  IP Address ***************")
pattern=r'((\d+\.){3}(\d+))'
ret=re.search(pattern,hist)
if ret:
    print("search pattern =  %r , ret  =  %r" % (pattern,ret.groups()))
else:
    assert ret is None, "IP address is not configured"

def find_IPv4(buffer):
    pattern=r'((\d+\.){3}(\d+))'
    ret=re.findall(pattern,buffer)
    if ret:
        print("find_IPv4 findall pattern =  %r , ret  =  %r" % (pattern,ret))
    else:
        assert ret is None, "IP address is not configured"
        return None

    # Validate
    for i in ret:
        print(i[0])
        ipv4=i[0]
        tmp=ipv4.split(".")
        if len(tmp) != 4 or int(tmp[0])<=0 or int(tmp[0])>255:
            print("%r is not valid" % (ipv4))
            continue
        try:
            valid = all(0 <= int(x) < 256 for x in tmp[1:3])
            print("%r is valid %r" % (ipv4,valid))
        except ValueError:
            print("%r is not valid" % (ipv4))

find_IPv4(hist)
