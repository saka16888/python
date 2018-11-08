def test_for():
    numbers = [11, 22, 33, 44]
    print ('before: %s' % numbers )
    for idx, item in enumerate(numbers,0):
        print('idx = %d' % idx)
        numbers[idx] *= 2
    print ('after: %s' % numbers)

test_for()

fruits = ['Banana', 'Apple', 'Lime']
print(list(enumerate(fruits)))

def test2():
    numbers = {11, 22, 33, 44}
    print ('before: %s' % numbers)
    for idx, item in enumerate(numbers,0):
        print('idx = %d' % idx)
        numbers[idx] *= 2
    print ('after: %s' % numbers)

# test2()