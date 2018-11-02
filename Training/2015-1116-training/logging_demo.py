'''
We stole the design of the logging module from Java.
It is enterprisy, full-featured, and huge!  It does
just about everything logging folks have ever wanted.

USING the logging module is easy.   CONFIGURING logging
involves a myriad of options.

'''

import logging

LOGGER = logging.getLogger(__name__)

logging.basicConfig(
    level = logging.INFO,
    format = '%(levelname)-8s | %(name)13s | %(asctime)s | %(message)s',
)

LOGGER.warning('Oops, I did it again')
LOGGER.error('The CPU is melting')
LOGGER.info('The human head weighs 8 and 1/2 pounds')
LOGGER.debug('The inner loop ran %d times and consumed %d bytes', 246, 820)
LOGGER.critical('The tickets to the first showing of Star Wars is sold out')

a= 10,20
print('the old value is %d and the new value is %d' % a)
print(type(a))

pref = dict(raymond='red', rachel='blue')
print(pref['raymond'])
try:
    print(pref['matthew'])
except KeyError as e:
    print('Matthew does not have a preference')
    print('The arguments are:', e.args)

try:
    print(pref['matthew'])
except KeyError:
    logging.exception('Matthew does not have a preference')
