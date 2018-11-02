__author__ = 'mihung'

# Test Objective:  Make sure there was no packet loss

from parsers import parse_ping

with open('notes/ping_output.txt') as f:
    output = f.read()                           # output = ubuntu.execute('ping www.cisco.com')
ping_result = parse_ping(output)
assert ping_result.loss_rate == 0.0
