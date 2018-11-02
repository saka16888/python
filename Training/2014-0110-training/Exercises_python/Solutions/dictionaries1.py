
def test():
    """Create and perform various operations on dictionaries."""
    dict1 = {}
    print 'Empty dictionary: %s' % (dict1, )
    dict2 = {'tomato': 'red', 'eggplant': 'purple'}
    print 'Another dictionary: %s' % dict2
    dict2['pepper'] = 'yellow'
    print 'Updated dictionary: %s' % dict2
    dict3 = {'cucumber': 'green', 'tomato': 'yellow stripes'}
    print 'One more: %s' % dict3
    dict3.update(dict2)
    print 'Updated: %s' % dict3
    print 'Keys: %s' % dict3.keys()
    print 'Values: %s' % dict3.values()
    print 'Items: %s' % dict3.items()
    print 'Length: %d' % len(dict3)
    print 'Keys and values:'
    for key in dict3:    # or dict3.keys()  or dict3.iterkeys()
        print '    Key: %s  Value: %s' % (key, dict3[key], )
    print 'Keys and values again:'
    for key, value in dict3.iteritems():
        print '    Key: %s  Value: %s' % (key, value, )
    print 'Cucumber: %s' % dict3.get('cucumber')
    print 'Cantelope: %s' % dict3.get('cantelope')
    print 'Cantelope: %s' % dict3.get('cantelope', -1)
    dict4 = {}
    dict4.setdefault('watermelon', 'empty')
    print '1. dict4: %s' % dict4
    dict4.setdefault('watermelon', 'other')
    print '2. dict4: %s' % dict4
    data1 = [('aa', 11), ('bb', 22), ('cc', 33), ]
    dict5 = {}
##     for tpl in data1:
##         dict5[tpl[0]] = tpl[1]
    for k, v in data1:
        dict5[k] = v
    print 'dict5:', dict5
    dict6 = dict(data1)
    print 'dict6:', dict6


if __name__ == '__main__':
    test()
