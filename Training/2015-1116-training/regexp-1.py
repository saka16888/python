__author__ = 'mihung'
import re

with open('notes/team_history.txt') as f:
    hist = f.read()
print(hist,"\n")
#----------------------------------------------------------------------------------------------------------
print("#" * 30,"--------------Error--------------", "#" * 30)
pattern=r'segment[\w]* fault'
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist,re.I)))
pattern=r'segment[\w]*fault'
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist,re.I)))
pattern=r'segment[ \w]*fault'
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist,re.I)))
pattern=r'segment[\w\s]*fault'
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist,re.I)))
pattern=r'segment[\w]*'
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist,re.I)))

print("\n","#" * 30,"-------------- quotes --------------", "#" * 30)
string = "TEMPLATES = ( ('index.html', 'home'), ('base.html', 'base'))"
print(re.findall(r'\(*\)', string))
print(re.findall(r'\([^()]*\)', string))

print(re.findall(r'\(abc\)#',hist))
print(re.findall(r'\(abc\) *#',hist))
print(re.findall(r'\((\w+)\).\((\w+)\)#',hist))
print(re.findall(r'\((\w+)\) \((\w+)\) #',hist))
print(re.findall(r'\([^()]*\)', hist))
print(re.findall(r'(abc)*#',hist))

print(re.findall(r'team',hist))
print(re.findall(r'te.m',hist))
print(re.findall(r'\bme\b',hist))
print(re.findall(r'\bwe\b',hist))
print(re.findall(r'[aeiou]',hist))
print(re.findall(r'[aeiouAEIOU]',hist))
print(re.findall(r'[0-9]',hist))
print(re.findall(r'\d*',hist))
print(re.findall(r'^[0-9]',hist))

print('*' * 40)
print(re.findall(r'\d+\s*point',hist))
print(re.findall(r'\d+/\d+/d+',hist))


print(re.findall(r'''
\d+    # Number
/       # Slash
\d+    # Number
/       # Slash
\d+     # Number
''', hist, re.VERBOSE ))

print(re.findall(r'[0-9]+/[0-9]+/[0-9]+',hist))

mo=re.findall(r'(\d+)/(\d+)/(\d+)',hist)
#if mo:
    #print(mo.group(0))
    #print(mo.group(1))
    #print(mo.group(2))
    #print(mo.group(3))
    # month,day,year = map(int,mo.groups())

print(re.findall(r'p.*s',hist))
print(re.findall(r'p.*?s',hist))
print(re.findall(r'p.*s',hist),re.DOTALL)

print(re.findall(r'^/* [A-Za-z]+',hist))
print(re.findall(r'^/* [A-Za-z]+',hist, re.MULTILINE))

print(re.findall(r'won|lost',hist, re.MULTILINE))
print(re.findall(r'\d+ point',hist))
print(re.findall(r'(\d+) point',hist))


