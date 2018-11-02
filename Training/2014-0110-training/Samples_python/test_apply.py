def apply(fn, numbers):
    acc = []
    for num in numbers:
        acc.append(fn(num))
    return acc


def fn1(x):
    return x * 3

def test():
    numbers = [11, 22, 33, 44]
    result = apply(fn1, numbers)
    print 'result:', result

test()
