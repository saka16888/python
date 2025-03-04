import argparse
#import pexpect

parser = argparse.ArgumentParser()

'''
parser.add_argument("square", help="display a square of a given number")

result:
Traceback (most recent call last):
  File "prog.py", line 5, in <module>
    print(args.square**2)
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
'''
parser.add_argument("--console_ip", help="console IP address")
parser.add_argument("--console_port", help="console port number")
parser.add_argument("--tftp_ip", help="TFTP server  IP address")
parser.add_argument("--image", help="path/image")

args = parser.parse_args()
print(args.console_ip)
print(args.console_port)
print(args.tftp_ip)
print(args.image)
