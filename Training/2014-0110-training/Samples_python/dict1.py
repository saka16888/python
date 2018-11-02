
d = {
    'bertrand': [1, 2, 3],
    'adele': [4, 5, 6],
    }
    
def test():
    for key in d.keys():
        print('key: %s' % key)
        for item in d[key]:
            print('    item: %d' % (item) )

if __name__ == '__main__':
   test()
#    config = {physicalTestbed: 'test_onl1'}
#   config = {'physicalTestbed': 'test_onl1',
#             'testbed': {'alias': 'tb-ag-1',
#                          'type': 'Physical',
#                          'name': 'testbed-ag-1'},}

   config = {'physicalTestbed': {'name': 'test_onl1'},
             'testbed': {'alias': 'tb-ag-1',
                          'type': 'Physical',
                          'name': 'testbed-ag-1'},
             'devices': {'AG6248-35': {'connections': {'ip': '10.62.2.251',
                                                        'protocol': 'telnet',
                                                        'port': 1035},
                                        'alias': 'rtr1',
                                        'management_ip': '10.62.2.35',
                                        'deviceType': 'LINUX',
                                        'credentials': {'username': 'root', 'password': 'onl'}}},
             'topology': {'AG6248-35': {'interfaces': {
                  '0/11': {'alias': 'rtr1-intf1', 'link': 'rtr1-1', 'ipv4': '1.2.3.1/24', 'type': 'ethernet'},
                  '0/12': {'alias': 'rtr1-intf2', 'link': 'rtr1-2', 'ipv4': '1.2.4.1/24', 'type': 'ethernet'}}}}}

   for key in config.keys():
        print("key = ",key)
