#!/usr/bin/env python

"""
Synopsis:
    Given a list of 2-tuples, process each item in the list in an
    order such that each item in the list is processed after the
    tuple whose first item is equal to the current tuple's second
    item, unless the tuple's second item is None, in which case it
    can always be processed.  In other words:

        1. Process (xx, bb) only after processing (bb, yy).
        2. Process (xx, None) in any order.

    Here is a sample list of tuples::

        Data1 = [
            ('aaa', 'mmm'),
            ('bbb', 'lll'),
            ('mmm', None),
            ('ccc', 'kkk'),
            ('lll', None),
            ('ddd', 'jjj'),
            ('iii', None),
            ('eee', 'aaa'),
            ('jjj', None),
            # comment out the following line to test for endless loop error.
            ('kkk', None),
        ]
Usage:
    python ordered_processed_list.py
"""

import sys

Data1 = [
    ('eee', 'aaa'),
    ('aaa', 'mmm'),
    ('bbb', 'lll'),
    ('mmm', None),
    ('ccc', 'kkk'),
    ('lll', None),
    ('ddd', 'jjj'),
    ('iii', None),
    ('jjj', None),
    # comment out the following line to test for endless loop error.
    ('kkk', None),
]

# An evil ordering.  Causes maximum recursion/iteration.
Data2 = [
    ('lll', 'mmm'),
    ('kkk', 'lll'),
    ('jjj', 'iii'),
    ('iii', 'hhh'),
    ('hhh', 'ggg'),
    ('ggg', 'fff'),
    ('fff', 'eee'),
    ('eee', 'ddd'),
    ('ddd', 'ccc'),
    ('ccc', 'bbb'),
    ('bbb', 'aaa'),
    ('aaa', 'mmm'),
    ('mmm', None),
]


def process_list1(in_data, processed, iteration=1):
    """Ordered processing using a list for lookup and recursion."""
    delayed = []
    count = 0
    for item in in_data:
        if item[1] is None or item[1] in processed:
            print 'processing --', iteration, item[0], item[1]
            processed.append(item[0])
            count += 1
        else:
            delayed.append(item)
    if count < 1:
        print 'missing item; cannot continue'
    elif delayed:
        process_list1(delayed, processed, iteration + 1)


def process_list2(in_data, processed, iteration=1):
    """Ordered processing using a set for lookup and recursion."""
    delayed = []
    count = 0
    for item in in_data:
        if item[1] is None or item[1] in processed:
            print 'processing --', iteration, item[0], item[1]
            processed.add(item[0])
            count += 1
        else:
            delayed.append(item)
    if count < 1:
        print 'missing item; cannot continue'
    elif delayed:
        process_list2(delayed, processed, iteration + 1)


def process_list3(in_data):
    """Ordered processing using a set for lookup and
    using while for iteration instead of recursion.
    """
    iteration = 0
    processed = set()
    while True:
        iteration += 1
        delayed = []
        count = 0
        tried = 0
        for item in in_data:
            tried += 1
            if item[1] is None or item[1] in processed:
                print 'processing --', iteration, item[0], item[1]
                processed.add(item[0])
                count += 1
            else:
                delayed.append(item)
        if count < 1:
            if tried > 0:
                print 'missing item; cannot continue'
                break
            else:
                # finished
                break
        else:
            # more to process
            in_data = delayed


def process_list4(in_data):
    """Ordered processing using a set for lookup and
    using while for iteration instead of recursion.
    This function uses yield to produce a generator that produces
    the items to be processed.
    """
    iteration = 0
    processed = set()
    while True:
        iteration += 1
        delayed = []
        count = 0
        tried = 0
        for item in in_data:
            tried += 1
            if item[1] is None or item[1] in processed:
                yield (iteration, item)
                processed.add(item[0])
                count += 1
            else:
                delayed.append(item)
        if count < 1 and tried > 0 and delayed:
                print 'missing item; cannot continue'
                break
        elif not delayed:
            # finished
            break
        else:
            # more to process
            in_data = delayed


def test():
    args = sys.argv[1:]
    if len(args) != 0:
        sys.exit(__doc__)
    print 'Using process_list1'
    process_list1(Data1, [])
    print '+-' * 30
    print 'Using process_list2 and a set'
    process_list2(Data1, set())
    print '+-' * 30
    print 'Using process_list3'
    process_list3(Data1)
    print '+-' * 30
    print 'Using process_list2 and a set'
    process_list2(Data2, set())
    print '+-' * 30
    print 'Using process_list3'
    process_list3(Data2)
    print '+-' * 30
    print 'Using process_list4 -- a generator function'
    for iteration, (item1, item2) in process_list4(Data2):
        print 'generating --', iteration, item1, item2


if __name__ == '__main__':
    #import ipdb; ipdb.set_trace()
    test()
