n1 = [11, 22, 33, 0, 44, 55, 66, ]
def test(numbers):
    #numbers = [11, 22, 33, 0, 44, 55, 66, ]
    print('numbers: %r' % numbers)
    sum = 0
    for item in numbers:
        if item == 0:
            break
        sum += item
    print('sum: %d' % (sum, ))

test(n1)
print(sum(n1))
