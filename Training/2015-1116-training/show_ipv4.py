__author__ = 'mihung'
'Learn to parse the column-oriented text typical of output from the Cisco IOS'

# Goal:  Show neatly formatted output with the ipaddr and interface with the status is up.
from parsers import parse_interfaces

with open('notes/ipv4_int_bri.txt') as f:
    output = f.read()                             # dev.execute('show ipv4 int bri')
for interface in parse_interfaces(output):
    if interface.status== 'up':
        print('%-15s %s' % (interface.ipaddr, interface.interface))
