__author__ = 'mihung'

import re

with open('../notes/team_history.txt') as f:
    hist = f.read()
print(hist)

'''Our team history:

* On 3/14/2013, we scored 14 points and lost the game.
* On 6/2/2013, we scored 15 points and lost the game.
* On 9/15/2013, we scored only 1 point and won the game.

234
Ip address 192.168.1.156
Ipv6 address 1:ef:::34:23
Go figure!
'''

print("-" * 40)
''' IPv6 pattern '''
IPv6_pat=r'''Ipv6 address (([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))'''
s=re.findall(IPv6_pat,hist)
print("Ipv6 address = ",s)

''' IPv4 pattern '''
IPv4_pat=r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
s=re.findall(IPv4_pat,hist)
print("Ipv4 address = ",s)

#-------------------------------------------------------------------------
print("-" * 40)
s=re.findall(r'team',hist)
print("team"," s = ",s)

print("-" * 40)
print(re.findall(r'te.m',hist))
print(re.findall(r'te*m',hist))
print(re.findall(r'\bme\b',hist))
print(re.findall(r'\bwe\b',hist))
print(r"(\w)(\1) ",re.findall(r'(\w)(\1)',hist))
#print(re.findall(r'[a-zA-Z0-9_](\1)',hist))
#-------------------------------------------------------------------------
print("-" * 40)
print(re.findall(r'[aeiou]',hist))
print(re.findall(r'[aeiouAEIOU]',hist))
print(re.findall(r'[0-9]',hist))
print(re.findall(r'\d*',hist))
print(re.findall(r'^[0-9]',hist))

#-------------------------------------------------------------------------
print("-" * 40)

print(re.findall(r'\d+\s*point',hist))
print(re.findall(r'\d+/\d+/d+',hist))
#-------------------------------------------------------------------------
print("+" * 40)

print(re.findall(r'''
\d+    # Number
/       # Slash
\d+    # Number
/       # Slash
\d+     # Number
''', hist))

print("re.VERBOSE ",re.findall(r'''
\d+    # Number
/       # Slash
\d+    # Number
/       # Slash
\d+     # Number
''', hist, re.VERBOSE ))

print('date : [0-9]+/[0-9]+/[0-9]+  %s' % re.findall(r'[0-9]+/[0-9]+/[0-9]+',hist))
#-------------------------------------------------------------------------
print("-" * 40)
print(r'(\d+)/(\d+)/(\d+) = ',re.findall(r'(\d+)/(\d+)/(\d+)',hist))

#-------------------------------------------------------------------------
print("-" * 40)

mo=re.search(r'On (\d+)/(\d+)/(\d+)',hist)
print(type(mo))
if mo:
    print(mo.group(0))
    print(mo.group(1))
    print(mo.group(2))
    print(mo.group(3))

mo=re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b',hist)
print(type(mo))
if mo:
    print(mo.group(0))
'''
mo=re.search(r'^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$',hist)
print(type(mo))
if mo:
    print(mo.group(0))
    print(mo.group(1))
    print(mo.group(2))
    print(mo.group(3))
'''


print("-" * 40)
month,day,year = map(int,mo.groups())
print(re.findall(r'p.*s',hist))
print(re.findall(r'p.*?s',hist))
print(re.findall(r'p.*s',hist),re.DOTALL)

print(re.findall(r'^/* [A-Za-z]+',hist)),
print(re.findall(r'^/* [A-Za-z]+',hist, re.MULTILINE))

print(re.findall(r'won|lost',hist, re.MULTILINE))
print(re.findall(r'\d+ point',hist))
print(re.findall(r'(\d+) point',hist))


