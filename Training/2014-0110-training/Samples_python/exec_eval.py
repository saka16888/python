def fn1(val):
    return val * 2


def test():
    x = 3
    y = 2
    expr = "fn1(x) + y + 4"
    result = eval(expr)
    print 'result:', result
    stmt = '''
print 'hello'
print fn1(3)
print 'goodbye'
'''
    exec stmt


test()
