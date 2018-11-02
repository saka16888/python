
"""
Print all the lines in a file followed by a line count.
"""


def test():
    count = 0
    infile = open('file1.py', 'r')
    for line in infile:
        count += 1
        line = line.rstrip()
        # right justified
        print 'line %2d: "%s"' % (count, line, )
        # left justified
        # print 'line %-2d: "%s"' % (count, line, )
        # zero filled
        # print 'line %02d: "%s"' % (count, line, )
    print '-' * 40
    print 'line count: %d' % count

if __name__ == '__main__':
    test()
