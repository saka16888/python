__author__ = 'mihung'

import re

with open('notes/team_history.txt') as f:
    hist = f.read()
print(hist,"\n")

#----------------------------------------------------------------------------------------------------------
USER_NAME_PROMPT = 'Username:'
ONL_USER_NAME = "root"
ONL_PASSWORD = "onl"
ICOS_USER_NAME = "admin"
ICOS_PASSWORD = "broadcom"
OS_LIST = ["onl","icos"]
OS_USER_NAME = [ONL_USER_NAME,ICOS_USER_NAME]
OS_PASSWORD =  [ONL_PASSWORD ,ICOS_PASSWORD ]
OS_choice = 0

LOCALHOST = 'localhost'
LOCALHOST = "[-_\w]*"
LAST_LOGIN = 'Last [lL]ogin: [\w]*'
LOGIN_PROMPT = '[lL]ogin:'
#LOGIN_PROMPT = LOCALHOST + ' [lL]ogin:'
USER_PROMPT = '[uU]ser:'
PASSWORD_PROMPT = '[pP]assword:'
LOGIN_INCORRECT='Login incorrect'
SU_LOGIN_PROMPT = '\[sudo\] password for [\w]*:'

NEW_LINE_CHARACTER = '\r\n'
SHOW_RUN_CMD = 'show run'
CLI_ERROR_MESSAGES = 'incorrect password attempts'
USER_EXEC_MODE_PROMPT = '@[-\w_]*:[\w~/-]*[#]'
LOCALHOST_EXEC_MODE_PROMPT = LOCALHOST+':~#'

LOCALHOST_EXEC_MODE_PROMPT = 'localhost:~#'
ICOS_LOCALHOST_EXEC_MODE_PROMPT = '\(' + 'localhost' + '\)' + ' #'
ICOS_LINUX_EXEC_MODE_PROMPT = '[\w-]*:[\w~/-]*\$'
ICOS_PASSWORD_PROMPT = 'password *'
ICOS_EXEC_MODE_PROMPT = '\(' + LOCALHOST + '\)' + ' #'
ICOS_CONFIG_MODE_PROMPT = r'\([^()]*\) *#'
ICOS_INIT_CONSOLE_PROMPT = 'Initializing console session'
ICOS_EXIT_PROMPT = r'(' + LOCALHOST + r') ' + '>'

#----------------------------------------------------------------------------------------------------------
print("#-------------- login--------------#")
pattern=LOGIN_PROMPT
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))
pattern=LAST_LOGIN
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))

#----------------------------------------------------------------------------------------------------------
print("#-------------- ICOS prompt--------------#")
pattern=ICOS_LINUX_EXEC_MODE_PROMPT
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))
pattern=ICOS_EXEC_MODE_PROMPT
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))
pattern=ICOS_CONFIG_MODE_PROMPT
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))

#----------------------------------------------------------------------------------------------------------
print("#--------------ONL prompt--------------#")
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

#----------------------------------------------------------------------------------------------------------
print("#-------------- ICOS prompt--------------#")
pattern = SU_LOGIN_PROMPT
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))

pattern=r'[\w~/-]*\$'
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))

pattern=r'[~\w/]*\$'
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))

pattern=r'[\w-]*:[\w~/-]*\$'
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))

pattern='[\w-]*:[\w~/-]*\$'
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))

pattern=ICOS_CONFIG_MODE_PROMPT
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))

#----------------------------------------------------------------------------------------------------------
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

#----------------------------------------------------------------------------------------------------------
print("#--------------DIAG prompt--------------#")
pattern=r'-DIAG>'
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))

pattern='[-\w_]*->'
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
pattern=r'[^>#\n]+#'
ret = re.search(pattern,hist)
if ret:
    print("pattern= %s , ret.group = %s" % (pattern, ret.group()))
    #print("ret.group(0) = ", ret.group(0));
    #print("ret.group(1) = ", ret.group(1));

pattern='[[fF]ail|[eE]rror]'
pattern='fan|cpu'
print("pattern= %s , re.findall = %s"% (pattern, re.findall(pattern,hist)))
ret = re.search(pattern,hist, re.I)
if ret:
    print("pattern= %s , ret.group = %s" % (pattern, ret.group()))
    #print("ret.group(0) = ", ret.group(0));
    #print("ret.group(1) = ", ret.group(1));

