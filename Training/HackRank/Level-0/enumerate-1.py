'''
enumerate(sequence, [start=0])
sequence -- 一个序列、迭代器或其他支持迭代对象。
start -- 下标起始位置。
'''

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
print(list(enumerate(fruits,1)))
print(fruits[3])

def test2():
    numbers = {11, 22, 33, 44}
    print('before: %s' % numbers)
    #print(list(enumerate(numbers,1)))
    n=len(numbers)
    for idx, item in enumerate(numbers,1):
        print('idx = %d' % idx)
        numbers[idx%n] *= 2
    print('after: %s' % numbers)

test2()