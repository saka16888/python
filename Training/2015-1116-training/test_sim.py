__author__ = 'mihung'


import topology
import parsers

tb = topology.load('sim_test.yaml')
dev = tb.devices['pyats-asa-1']
dev.connect()
dev.config('''
    interface GigabitEthernet0/0
      nameif inside
      security-level 100
      ip address 10.0.0.1 255.255.255.0
      no shut
''')

########## Ping Tests #################################################
# Test Objective:  Verify that no packets are lost:  ping www.cisco.com

output = dev.execute('ping www.cisco.com')
ping_result = parsers.parse_ping(output)
assert ping_result.loss_rate == 0.0

########## IPV4 Interface Tests #######################################
output = dev.execute('show ipv4 int bri')
interfaces = parsers.parse_interfaces(output)

# Test objective 1:  "show ipv4 int bri" and verify that at least 5 interfaces have an "Up" status
assert sum([interface.status=='up' for interface in interfaces]) > 5

# Test objective 2:  "show ipv4 int bri" and verify no more that 6 of those are "unassigned"
assert sum([interface.ipaddr == 'unassigned' for interface in interfaces if interface.status=='up']) <= 6

# Test objective3:  "show ipv4 int bri" all"Shutdown" are "unassigned"
assert all(interface.ipaddr == 'unassigned' for interface in interfaces if interface.status == 'shutdown')

######### External Interface IRQ and MacAddr Tests ####################
output = dev.execute('show version')
interfaces = parsers.parse_external_interfaces(output)

# Test Objective 1:  Make sure the management interface is on irq 8, 10, 12, or 14
assert all(int(intf.irq) in allowed_mgmt_irqs for intf in interfaces if intf.interface == 'Management0/0')

# Test Objective 2:  Make sure that irq has no more than 2 interfaces
assert len([intf for intf in interfaces if intf.irq == '10']) <= 2

# Test Objective 3:  Verify that all macaddresses startwith 0050.5693
assert all(intf.macaddr.startswith('0050.5693') for intf in interfaces)

# Test Objective 4:  Verify that no interfaces in on a reserved irq:  2, 4, 6, 15
reserved_irqs = {2, 4, 6, 15}
assert {int(intf.irq) for intf in interfaces}.isdisjoint(reserved_irqs)

########### Licensed Features Tests ###################################
output = dev.execute('show version')
features = parsers.parse_licensed_features(output)

# Objective 1:  Make sure the Shared License is disabled
assert features['Shared License'].value == 'Disabled'

# Objective 2:  Make sure all settings have a renewal period set to "perpetual"
assert all(setting.renewal == 'perpetual' for setting in features.values())

# Objective 3:  Make sure the Failover is set to Active/Standby
assert features['Failover'].value == 'Active/Standby'

# Objective 4:  Make sure there are at least 200 UC Phone Proxy Sessions
assert int(features['UC Phone Proxy Sessions'].value) > 200

########### Cleanup ####################################################

dev.config('''
    clear config object
    clear config access-group
    clear config interface g0/0
''')

dev.disconnect()

