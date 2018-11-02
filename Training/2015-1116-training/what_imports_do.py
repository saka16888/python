'''

'''
__author__ = 'mihung'
x = 10

from random import randrange

def show_family(lastname, firstnames):
    print(lastname.upper())
    print('=' * len(lastname))
    for name in firstnames:
        print(name.title())
    print()

class Family:
    'Typical family'

if __name__ == '__main__':

    print(randrange(10000))

    f = Family()
    f.lastname = 'cleaver'
    f.fnames = ['ward', 'june', 'wally', 'theodore']

    show_family('hettingers', ['raymond', 'rachel', 'matthew'])
    show_family(f.lastname, f.fnames)
