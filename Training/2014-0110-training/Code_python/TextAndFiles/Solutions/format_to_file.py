#!/usr/bin/env python


"""
Format data and write to file.

Parse colon-delimited data.
Format.
Write to file.
"""

Data = """\
Alice Appleby:501-511-5111:1.5:bird watching
Bill Barnaby:501-511-5111:4009.2:gardening
"""

def test():
    outfile = open('tmp01.txt', 'w')
    outfile.write('Name                Phone            Level Hobby\n')
    outfile.write('====                =====            ===== =====\n')
    for line in Data.splitlines():
        s1 = format_line(line)
        outfile.write(s1)
    outfile.close()

def format_line(line):
    fields = line.split(':')
    if len(fields) == 4:
        name = fields[0].ljust(20)
        phone = fields[1].ljust(12)
        level = fields[2].rjust(10)
        hobby = fields[3].ljust(15)
        s1 = '%s%s%s %s\n' % (name, phone, level, hobby, )
    else:
        s1 = 'bad string'
    return s1

test()
