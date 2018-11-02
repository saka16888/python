#!/usr/bin/env python

Data1 = ('aaa', ('bbb', ('ccc', ('ddd', None))))


def walk1():
    walk1_helper(Data1)


# Recursive walk over single linked list.
# Not usually a good idea in a language that does not do
# tail recursion elimination, for example Python.
def walk1_helper(data):
    if data:
        print('(walk1) item:', data[0])
        walk1_helper(data[1])


# Iterate over single linked list.
def walk2():
    d1 = Data1
    while d1:
        print('(test1) item:', d1[0])
        d1 = d1[1]


def gen1(seq):
    while seq:
        yield seq[0]
        seq = seq[1]


# Use generator to iterate over single linked list.
def walk3():
    for item in gen1(Data1):
        print('(test2) item:', item)


def gen_next_str_pos(pat, instr):
    pos = instr.find(pat)
    while pos != -1:
        yield pos
        pos = instr.find(pat, pos + 1)


def test_gen_next_str_pos():
    pat = 'abc'
    target = '11abc22abc33abc44'
    for pos in gen_next_str_pos(pat, target):
        print('(test3) pos:', pos)


def main():
    test_gen_next_str_pos()


if __name__ == '__main__':
    main()
