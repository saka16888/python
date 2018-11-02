
"""
Provide a dummy module for testing.
"""

GlobalValue = 'some global value'

def test():
    print '__name__: "%s"' % __name__

if __name__ == '__main__':
    test()
