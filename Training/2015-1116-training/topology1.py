import yaml

from keyedlist import KeyedList
import sys

class Device:
    def __init__(self, devname, **kwargs): # <------------- +++++++++++++
        self.__dict__.update(kwargs)
    def connect(self):
        pass
    def execute(self, action):
        pass
    def config(self, s):
        pass
    def disconnect(self):
        pass

from sim import Device       # <------------- +++++++++++++

def load(filename):

    #1 Read the YAML file
    #  Potential problem:  Invalid YAML
    #  Solution:  Use try_yaml.py to figure-out the problem
    #             or just nudge it to become more JSON-like
    with open(filename) as f:
        tb = yaml.load(f)

    #2 Wrap the multi-level dict in a keyed list
    #  Purpose:  make lookups simpler using dots instead of square bracket
    tb = KeyedList(tb)

    #3 Schema validation -- Even if the YAML is valid, the keys might be misspelled
    #  Potential problem:  Unexpected keys
    #  Solution:  Fix the spelling of that key
    toplevel_schema = {'testbed', 'devices', 'topology'}
    if not set(tb) <= toplevel_schema:
        print('Bad top level keys: %r' % (set(tb.keys()) - toplevel_schema))
        sys.exit(1)

    testbed_schema = {'alias', 'custom', 'name', 'passwords', 'servers', 'tacacs'}
    if not set(tb['testbed']) <= testbed_schema:
        print('Bad top level keys: %r' % (set(tb['testbed']) - testbed_schema))
        sys.exit(1)

    #4 Replace some dictionary entries with classes
    for devname, devvalue in tb.devices.items():
        tb.devices[devname] = Device(devname, **devvalue)   # <------------- +++++++++++++

    return tb

if __name__ == '__main__':
    from pprint import pprint

    #tb = load('notes/example_topology.yaml')
    tb = load('asa_topo.yaml')
    pprint(tb)

    asa = tb.devices['asa-1']
    asa.connect(via='alt')
    asa.connect()
    asa.config('abc\n123\ndo re mi\n')
    output = asa.execute('show version')
    asa.disconnect()

    from parsers import *
    pprint(parse_external_interfaces(asa.execute('show version')))
    pprint(parse_licensed_features(asa.execute('show version')))
    pprint(parse_interfaces(asa.execute('show ipv4 int bri')))
    pprint(parse_ping(asa.execute('ping www.cisco.com')))


