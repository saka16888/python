def test_for():
    numbers = [11, 22, 33, 44]
    print('before: %s' % numbers)
    for idx, item in enumerate(numbers):
        numbers[idx] *= 2
    print('after: %s' % numbers)

test_for()
