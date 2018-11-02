def test():
    # remove duplicates
    print 'remove duplicates'
    a = [11, 22, 33, 22, 44, 33]
    nodups = list(set(a))
    print nodups

    list1 = range(0, 10)
    list2 = range(8, 20)
    set1 = set(list1)
    set2 = set(list2)
    union1 = set1 or set2
    union2 = set1 | set2
    union3 = set1.union(set2)
    intersection1 = set1 and set2
    intersection2 = set1 & set2
    intersection3 = set1.intersection(set2)
    difference = set1.difference(set2)
    exclusive_union = set1.union(set2).difference(set1.intersection(set2))

    print '-' * 20
    print 'union tests'
    print 5 in union1
    print 8 in union1
    print 5 in union2
    print 8 in union2
    print 5 in union3
    print 8 in union3
    print '-' * 20
    print 'intersection tests'
    print 5 in intersection1
    print 8 in intersection1
    print 5 in intersection2
    print 8 in intersection2
    print 5 in intersection3
    print 8 in intersection3
    print '-' * 20
    print 5 in difference
    print 12 in difference
    print '-' * 20
    print 5 in exclusive_union
    print 8 in exclusive_union

    print '-' * 20
    print 'equality or identity?'
    # this did not work.
    a1 = [11, 22]
    a2 = [11, 22]
    # this did
    a1 = frozenset([11, 22])
    a2 = frozenset([11, 22])
    print a1 == a2
    print a1 is a2
    b1 = [a1, a2]
    print set(b1)

test()
