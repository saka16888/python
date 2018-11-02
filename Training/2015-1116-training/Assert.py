import re

def checkNoError(data,keyword=[]):
    '''
        data : string
        keyword: the pattern user wants to search
        Return :
            False : if keyword is found in data
            True : if keyword is not found in data
        '''
    if keyword == []:
        #pattern = r"failed|traceback|segmentfault|can't open file"
        pattern_list = ["fail","traceback","segmentfault",r"can't open file"]
    else:
        pattern_list = keyword
    pattern=r'|'.join(pattern_list)
    ret = re.match(pattern, data, re.I)
    print("\npattern = %s , \ndata = %s, \nret = %s" % (pattern,data,ret))
    #return (False if ret != None else True)
    return (False if any(re.findall(pattern, data, re.I)) else True)

data="Error"
print(checkNoError(data))
#assert (not checkNoError(data)),format("%s  : found error" % data)

data=r"cant open file"
print(checkNoError(data))
#assert checkNoError(data),format("found error : %s " % data)

data=r"can't open file"
print(checkNoError(data))

data=r"open"
print(checkNoError(data))

data="Segment fault"
print(checkNoError(data))
#assert checkNoError(data),format("found error : %s " % data)

data="Segmentfault"
print(checkNoError(data))

data="fail"
print(checkNoError(data))

data="Test case failed"
print(checkNoError(data))
#assert checkNoError(data),format("found error : %s " % data)
data="Test case failed"
print(checkNoError(data,keyword=["fail",]))

data="Segmentfault  can't open file Test case failed"
print(checkNoError(data,keyword=["fail","segment","can't"]))

output = "final result : fail "
output = "python: can't open file 'LED_tc9.py': [Errno 2] No such file or directory"
#assert ("fail" not in output), " result : fail"
assert not ("fail" in output or "hello" in output), "result : fail"
#assert not ("fail" in output or "can't open file" in output), "result : fail"
#assert not ("fail" in output or "No such file" in output), "result : fail"
