
GlobalVariable1 = 'Help me'


def function1():
    flag = False
    function2(flag)


def function2(flag):
    if flag:
        y = x + 3
        print(y)
    else:
        print('ok')
        print(GlobalVariable1)


#function2()

function1()
