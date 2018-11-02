

class AttrDict(dict):
    ''' A cute trick to replace the instance dictionary with an inherited dictionary.

        Purpose is keep all the capabilites of a regular dict that we inherited,
        keys, values, items, square brackets, etc, BUT we also want the
        capability of the instance dictionary which is to dotted access like
        d.raymond=10.
        Limitations: You can only do dotted lookups on valid variable names.
        This works ``d['asa-10']`` but not this ``d.asa-10``.   Also, ``d['class']``
        works but not ``d.class``.  So, no hyphens, numbers, or reserved words.
    '''
    def __init__(self):
        self.__dict__ = self

if __name__ == '__main__':

    d = AttrDict()
    d['raymond'] = 'red'
    d['rachel'] = 'blue'
    d.matthew = 'yellow'
    d.becky = 'green'

    print(d)                  # inherited dict
    print(d.__dict__)         # instance dict

    print(d['raymond'])
    print(d['rachel'])
    print(d.matthew)
    print(d.becky)
    print(d.raymond)
    print(d.rachel)
    print(d['matthew'])
    print(d['becky'])

    testbed = {'name': 'testbed-wb-1', 'packetgenerator': {'rx_intf': 'enx803f5d08fd', 'tx_intf': 'eth1'}}
    print(testbed['packetgenerator']['rx_intf'],dir(testbed['packetgenerator']['rx_intf']))



