import re

with open('notes/team_history.txt') as f:
    hist = f.read()
print(hist,"\n")

#----------------------------------------------------------------------------------------------------------
print("#" * 30,"--------------ONL prompt--------------", "#" * 30)
USER_EXEC_MODE_PROMPT = '@[-\w_]*:[\w~/-]*[#|$]'
LOCALHOST_EXEC_MODE_PROMPT = 'localhost:~#'

pattern='[\w~/-]*'
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))

pattern='localhost:[\w~/]*#'
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))

pattern='[-\w_]*:[/\w~-]*#'
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))

pattern='[\-\w_]*:[/\w~-]*#'
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))

# failed case
pattern='[-\w_]*:[\w_~]*#'
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))

pattern='@[-\w_]*:[\w~/-]*#'
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))

pattern='[-\w_]*:[\w~/-]*#'
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))

pattern=r'[\w\-_]*:[\w~/-]*#'
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))

pattern=r'[\w\-_]*:[\w~/-]*[#|\$]'
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))

pattern=r'[\w\-_]*:[\w~/-]*[#|$]'
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))

print("#-------------- ICOS prompt--------------#")
LOCALHOST = 'localhost'
ICOS_LOCALHOST_EXEC_MODE_PROMPT = '\(' + 'localhost' + '\)' + ' #'
ICOS_EXEC_MODE_PROMPT = '[\w-]*:[\w~/-]*\$'
ICOS_PASSWORD_PROMPT = 'password *'
ICOS_EXEC_MODE_PROMPT = '\(' + LOCALHOST + '\)' + ' #'
ICOS_CONFIG_MODE_PROMPT = r'\([^()]*\) *#'
ICOS_INIT_CONSOLE_PROMPT = 'Initializing console session'
ICOS_EXIT_PROMPT = r'(' + LOCALHOST + r') ' + '>'

pattern=r'[\w~/-]*\$'
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))

pattern=r'[~\w/]*\$'
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))

pattern=r'[\w-]*:[\w~/-]*\$'
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))

pattern='[\w-]*:[\w~/-]*\$'
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))

print("#--------------ONIE prompt--------------#")
pattern=r'\|\*ONIE *\|'
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))

pattern=r'[|*]ONIE *\|'
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))

pattern=r'\|\*ONIE: Embed ON'
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))

pattern=r'\*ONIE: Embed ON'
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))

pattern=r'ONIE:/#'
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))

pattern=r'ONIE:/ #'
ret = re.search(pattern,hist)
if ret:
    print("pattern= %s , ret.group = %s" % (pattern, ret.group()))
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))

pattern=r'ONIE:/\s#'
ret = re.search(pattern,hist)
if ret:
    print("pattern= %s , ret.group = %s" % (pattern, ret.group()))
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))

pattern=r'ONIE:/\w* #'
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))

print("#--------------DIAG prompt--------------#")
pattern=r'-DIAG>'
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))

# Choose option
pattern=r'\|\*Open Network Linux'
ret = re.search(pattern,hist)
if ret:
    print("pattern= %s , ret.group = %s" % (pattern, ret.group()))

pattern=r'\|\*ONIE'
ret = re.search(pattern,hist)
if ret:
    print("pattern= %s , ret.group = %s" % (pattern, ret.group()))


# Cmd prompt
print("#" * 30,"-------------- re.search  prompt --------------", "#" * 30)
pattern=r'[^>#\n]+#'
ret = re.search(pattern,hist)
if ret:
    print("pattern= %s , ret.group = %s" % (pattern, ret.group()))
    #print("ret.group(0) = ", ret.group(0));
    #print("ret.group(1) = ", ret.group(1));

pattern=r'[^>@#\r\n]+#'
ret = re.search(pattern,hist,re.DEBUG)
if ret:
    print("pattern= %s , ret.group = %s" % (pattern, ret.group()))

pattern=r'(\w)+@[^>#\r\n]+#'
ret = re.search(pattern,hist)
if ret:
    print("pattern= %s , ret.group = %s" % (pattern, ret.group()))

pattern=r'(\w)*@[^>#\r\n]+#'
ret = re.search(pattern,hist)
if ret:
    print("pattern= %s , ret.group = %s" % (pattern, ret.group()))

pattern=r'@[^>#\n]+#'
ret = re.search(pattern,hist)
if ret:
    print("pattern= %s , ret.group = %s" % (pattern, ret.group()))


mac_address= r'/^([0-9a-f]{1,2}[\.:-]){5}([0-9a-f]{1,2})$/i'

print("mac_address = ", re.findall(r'^([[:xdigit:]]{2}[:.-]?){5}[[:xdigit:]]{2}$', hist))
print("mac_address = ", re.findall(r'([0-9A-F]{2}[:.-]){5}([0-9A-F]{2})', hist))
