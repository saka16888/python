#!/usr/bin/env python
"""
Format data and write to screen.

Parse colon-delimited data.
Format.
Print to screen.
"""

Data = """\
Alice Appleby:501-511-5101:1.5:bird watching
Bill Barnaby:501-511-5102:4009.2:gardening
Charlie Carbunkle:501-5103:54.251:hiking and bicycling
"""

def test():
    print 'Name                Phone            Level Hobby'
    print '====                =====            ===== ====='
    for line in Data.splitlines():
        s1 = format_line(line)
        print s1

def format_line(line):
    fields = line.split(':')
    if len(fields) == 4:
        name = fields[0].ljust(20)
        phone = fields[1].ljust(12)
        level = fields[2].rjust(10)
        hobby = fields[3].ljust(30)
        s1 = '%s%s%s %s' % (name, phone, level, hobby, )
    else:
        s1 = 'bad string'
    return s1

test()
