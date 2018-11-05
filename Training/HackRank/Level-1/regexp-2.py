import re
def simpleValidateIPv4(hostIP):
    pat = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    test = pat.match(hostIP)
    print("test = ",test.group())
    if test:
       print(hostIP," Acceptable ip address")
    else:
       print(hostIP," Unacceptable ip address")

def accurateValidateIPv4(hostIP):
    pat = re.compile("^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
    test = pat.match(hostIP)
    if test:
       print(hostIP," Acceptable ip address")
    else:
       print(hostIP," Unacceptable ip address")

print(simpleValidateIPv4("1.1.1.2"))
print(simpleValidateIPv4("555.1.1.2"))
print(simpleValidateIPv4("256.1.1.2"))

print(accurateValidateIPv4("256.1.1.2"))

s1 = 'height: 123.45 width: 456'
r1 = re.search(r'height: (\d*.\d*) width: (\d*)', s1)
print(r1.group(0))
print(r1.group(1))
print(r1.group(2))

print(40 * "-")
s2 = "Ip address 12.3.45.12, Ip address 53.434.433.44"
pat1 = re.findall(r'Ip address (\d*.\d*.\d*.\d*)',s2)
print("pat1 = ",pat1)
print("pat1[0] =",pat1[0],"\n")

print(40 * "-")
pat = re.compile('Ip address (\d*.\d*.\d*.\d*)')
r2 = pat.search(s2)
if r2:
    print(r2.group(0))
    print(r2.group(1))
print(type(r2))

print(40 * "-")
s3 = "IP address 12.3.45.12"
pat = re.compile('^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$')
print("s3 = ",s3, "pat = ",pat)
r3 = pat.search(s3)
if r3:
    print(r3.group(0))
    print(r3.group(1))

s = "Number of 123 pkts/sec"
r4 = re.search(r'(\d*) pkts/sec', s)
print(type(r4))
if r4:
    print(r4.group(0))
    print(r4.group(1))
