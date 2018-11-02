def test():
    data1 = ['apples', 'tangerines', 'grapes', 'apricots', ]
    target = 'grapes'
    found = None, None

    for index, item in enumerate(data1):
        if item == target:
            found = index, target
            break

    #found=[index, target if item == target: for index, item in enumerate(data1)]
    print('1. found -- {} {}'.format(found[0], found[1]))
    target = 'blueberries'
    found = None, None
    for index, item in enumerate(data1):
        if item == target:
            found = index, target
            break
    print('2. found -- {} {}'.format(found[0], found[1]))
    target = 'tangerines'
    for index, item in enumerate(data1):
        if item == target:
            found = index, target
            break
    else:
        found = None, None
    print('3. found -- {} {}'.format(found[0], found[1]))
    target = 'blueberries'
    for index, item in enumerate(data1):
        if item == target:
            found = index, target
            break
    else:
        found = None, None
    print('4. found -- {} {}'.format(found[0], found[1]))


test()
