''' High-speed whirlwind tour of Python.
    No time to stop and linger.
    Just watch it go by in a blur.
    We'll go into the details later.
'''

print('My name is:', __name__)
print('What can I do?\n', __doc__)

''' This is description '''

print('What s next?\n', __doc__)

if __name__ == '__main__':
    print('Usually, we put test code in this section')


#### Dictionaries #########################################

brands = {
    'raymond': 'mac',
    'rachel': 'pc',
    'matthew': 'vtech',
}

print(type(brands))          # show type
print(len(brands))           # show size
print(brands)                # show contents
print(brands['rachel'])      # key lookup
brands['matthew'] = 'asus'   # store a new key/value pair
del brands['raymond']        # remove a key
print('matthew' in brands)   # membership test
print(brands)

print(brands.keys())
print(brands.values())
print(brands.items())

#### File and URL Handling #################################

with open('hamlet.txt') as f:
    play = f.read()
    print(len(play))

import urllib.request

with urllib.request.urlopen('http://jython.org') as u:
    page = u.read()
    print("len of page",len(page),"page",page)

#### Slicing ###############################################

print(play[:400])
print(page[:400])

#### Access Styles #########################################

# LBYL -- Look before you leap
if 'becky' in brands:
    print(brands['becky'])
else:
    print('Becky is not in the brands dictionary')

# EAFP -- Easier to ask forgiveness than permission
try:
    print(brands['becky'])
except KeyError:
    print('Becky is not in the brands dictionary')    

#### How to use threads #####################################

import threading

printer_lock = threading.Lock()

#### How to use locks #######################################

with printer_lock:      # Acquires on the way in and releases on the way out
    print('Critical section 1')
    print('Critical section 2')

#### Object oriented Programming ###########################

class Computer:
    'Number compute machine'

    kind = 'electrical gizmo'

c = Computer()
d = Computer()
e = Computer()

c.brand = 'HP'
d.brand = 'Lenovo'
e.brand = 'Dell'

Computer.size = 10

computers = [c, d, e]
for computer in computers:
    print('The %s is a %s' % (computer.kind, computer.brand))

#### Encoding and Decoding (convert to and from a string or bytes)

import json             # JSON is simple, fast, and language independent but it is restricted lists and dicts
import pickle           # Pickle is Python specific but it handles many more object types
import urllib.parse     # Simple and standard but only used for urls
#import yaml             # More complex than JSON, less universal than JSON, slower than JSON, easier to type than JSON

s1 = json.dumps(brands)
s2 = pickle.dumps(brands)
s3 = urllib.parse.urlencode(brands)
#s4 = yaml.dump(brands)

del brands

b1 = json.loads(s1)
b2 = pickle.loads(s2)
b3 = urllib.parse.parse_qsl(s3)
#b4 = yaml.load(s4)

