numbers = [11, 22, 33, 44, ]
print('before: %s' % (numbers,))

def test_while():
    idx = 0
    while idx < len(numbers):
        numbers[idx] *= 2
        idx += 1
    print('after: %s' % (numbers))

test_while()

def enumerate1(x):
    v=[]
    for idx,val in enumerate(x):
        v.append(idx+val)
    print('v=',v)

enumerate1(numbers)
