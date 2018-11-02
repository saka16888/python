__author__ = 'mihung'

'Collection of reusable parsing utilities'

import re
from collections import namedtuple

class NoMatch(KeyError):
    'Exception raised when an expected pattern is not found'

Interface = namedtuple('Interface', ['interface', 'ipaddr', 'status', 'protocol'])
ExternalInterface = namedtuple('ExternalInterface', ['port', 'interface', 'macaddr', 'irq'])
PingResult = namedtuple('PingResult', ['transmitted', 'received', 'loss_rate'])

def parse_interfaces(output):
    ''' Parse the output of ``show ipv4 interfaces brief``.
        Return a list of named tuples in the form ``Interface(interface, ipaddr, status, protocol)``.
    '''
    interfaces = []
    for line in output.splitlines():
        interface = Interface(line[:31].rstrip(),
                              line[31:47].rstrip(),
                              line[47:69].rstrip().lower(),
                              line[69:].rstrip().lower())
        interfaces.append(interface)
    return interfaces

def parse_external_interfaces(output):
    '''Parse the output of ``show version``
       Return a list of tuples in the form ``ExternalInterface(port, interface, macaddr, irq')
    '''
    ext_intf_pattern = r'^\s*(\d+): Ext: (\S+)\s+: address is ([0-9A-Za-z.]{14}), irq (\d+)$'
    interfaces = []
    for port, interface, macaddr, irq in re.findall(ext_intf_pattern, output, re.MULTILINE):
        ext_intf = ExternalInterface(port, interface, macaddr.lower(), irq)
        interfaces.append(ext_intf)
    return interfaces

def parse_ping(output):
    'Parse the output of a ``ping` in to a PingResult named tuple'
    ping_result_pattern = r'(\d+) packets transmitted, (\d+) packets received, ([0-9.]+)% packet loss'
    mo = re.search(ping_result_pattern, output)
    if mo is None:
        raise NoMatch(ping_result_pattern, output)
    transmitted, received, loss_rate = mo.groups()
    return PingResult(int(transmitted), int(received), float(loss_rate))
