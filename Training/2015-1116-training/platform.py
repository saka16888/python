import os, re
LIB_ONLP = ''
def platform():
    f = os.popen('echo x86_64')
    output = f.read()
    if re.search("x86_64",output):
        return '/lib/x86_64-linux-gnu/libonlp.so'
    elif re.search("arm",output):
        return '/lib/arm-linux-gnueabi/libonlp.so'
    else :
        return '/lib/x86_64-linux-gnu/libonlp.so'

LIB_ONLP=platform()
print(LIB_ONLP)