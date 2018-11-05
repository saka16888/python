def test_while():
    numbers = [11, 22, 33, 44, ]
    #print('before: %s' % (numbers, ))
    print('before: %s' % numbers)
    idx = 0
    while idx < len(numbers):
        numbers[idx] *= 2
        idx += 1
    print('after: %s' % (numbers, ))

test_while()