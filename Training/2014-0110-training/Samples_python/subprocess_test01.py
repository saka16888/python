#!/usr/bin/env python
"""
An example of the use of the subprocess module.
This example shows how to run a command (program) from within a
python script.
"""

from subprocess import Popen, PIPE


def test():
    proc = Popen(
        "./subprocess_process01.py",
        shell=True,
        stdin=PIPE,
        stdout=PIPE,
        stderr=PIPE,
        close_fds=True)
    proc.stdin.write("aaa bbb ccc\n")
    proc.stdin.write("ddd eee fff\n")
    proc.stdin.write("ggg hhh iii\n")
    proc.stdin.close()
    content = proc.stdout.readlines()
    print('length:', len(content))
    for line in content:
        print('line:', line.rstrip('\n'))

if __name__ == '__main__':
    test()
