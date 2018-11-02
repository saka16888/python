
import module_b
import module_c
import module_d


def test():
    print '1. %s' % module_c.get_value()
    module_b.modify('bbb')
    print '2. %s' % module_c.get_value()
    print '3. %s' % module_d.GLOBAL_1

if __name__ == '__main__':
    test()


