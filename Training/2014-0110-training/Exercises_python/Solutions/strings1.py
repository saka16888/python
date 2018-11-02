# vim: set fileencoding=utf-8 :

S1 = """peaches are pink
lemons are yellow
tomatoes are red
and i'm very mellow
"""

S2 = 'Selçuk'


def test():
    """Perform various operations on strings.
    """
    s1 = 'the brown dog is a frisky dog'
    print 's1:', s1
    print 'S1:', S1
    print 'I love tomatoes in the summertime\nI love apples in the fall\n'
    print 's1 + S1:', s1 + S1
    print 'len(s1):', len(s1)
    n1 = s1.find('dog')
    n2 = s1.find('dog', n1 + 1)
    print 'n1, n2:', n1, n2
    name = 'dave'
    category = 3
    intensity = 4.8
    s2 = '"%s" is in category %d with intensity %.3f' % (
        name, category, intensity, )
    print 's2:', s2
    print 'ljust: "%s"' % name.ljust(10)
    print 'rjust: "%s"' % name.rjust(10)
    s3 = '    abc def    \n'
    print 'lstrip: "%s"' % s3.lstrip()
    print 'rstrip: "%s"' % s3.rstrip()
    print 'strip: "%s"' % s3.strip()
    data = ['abc', 'def', 'ghi', 'jkl', ]
    print 'join:', '::'.join(data)
    # notice the encoding definition at the top of this file.
    # can also use:
    #    # coding=utf-8
    print 'len s4:', len(S2)
    s5 = S2.decode('utf-8')
    print 'len s5:', len(s5)
    s6 = s5.encode('utf-8')
    print 's6:', s6
    s7 = u'Sel\xe7uk'
    s8 = s7.encode('utf-8')
    print 's8:', s8


def collect(word, strings):
    acc = []
    for string in strings:
        if string.find(word) > -1:
            acc.append(string)
    return acc


def main():
    test()
    accum = collect('dog', ['each dog has his day', 'the cat is furry'])
    print 'accum from collect:', accum


if __name__ == '__main__':
    main()
