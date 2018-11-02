import sys


def count(filename):
    infile = open(filename, 'r')
    accum = {}
    for line in infile:
        line = line.rstrip()
        words = line.split()
        for word in words:
##             accum.setdefault(word, 0)
##             accum[word] += 1
            if word in accum:
                accum[word] += 1
            else:
                accum[word] = 1
    infile.close()
    return accum


def test():
    args = sys.argv[1:]
    filename = args[0]
    accum = count(filename)
    words = accum.keys()
    words.sort()
    for word in words:
        print 'word: "%s" -- count: %d' % (word, accum[word], )

test()
