"""
Synopsis:
    Create and use lightweight pseudothreads.
    Run several greenlets (instances of gevent Greenlets) in parallel.
    Implement a subclass of gevent.Greenlet.  When an instance of
        this subclass runs, it should (1) sleep for several seconds, and
        then (2) return a value.
    Create several instances of that class and run them.  Print the
        value returned by each greenlet.
Options:
    -h, --help              Print this help message.
    -c, --command <cmd>     Command to run.  Possibles values are
                              "empty" and "parsexml".
    -t, --threads <n>       Number of threads to start.
Arguments:
    For command "empty" -- n -- number of seconds to delay.
    For command "parsexml" -- filename.xml -- XML document to parse.
Usage:
    python greenlet1.py
    python greenlet1.py -c empty -t 10 2
    python greenlet1.py -c parsexml -t 100 people_big.xml
"""


import sys
import getopt
import gevent
from gevent import Greenlet
#from lxml import etree
#from xml.etree import ElementTree as etree
from xml.etree import cElementTree as etree


DEBUG = False


class MyGreenletError(Exception):
    pass


def dbgprint(msg):
    if DEBUG:
        print msg


class MyNoopGreenlet(Greenlet):

    def __init__(self, index, command, arg):
        Greenlet.__init__(self)
        self.index = index
        self.command = command
        self.arg = arg
        try:
            self.iarg = int(arg)
        except ValueError:
            pass

    def _run(self):
        dbgprint('starting -- %s' % self)
        if self.command == 'empty':
            self.empty_fn()
        elif self.command == 'parsexml':
            self.xml_parse_fn()
        else:
            raise MyGreenletError('cannot find command: "%s"' % self.command)
        dbgprint('leaving -- %s' % self)
        value = 'my value -- %s' % (self.index * 3, )
        return value

    def empty_fn(self):
        gevent.sleep(self.iarg)

    def xml_parse_fn(self):
        doc = etree.parse(self.arg)
        root = doc.getroot()
        print '%d. tag: "%s"' % (self.index, root.tag, )

    CommandTable = {
        'empty': empty_fn,
        'parsexml': xml_parse_fn,
    }

    def __str__(self):
        return 'MyNoopGreenlet(%s:%s)' % (self.index, self.arg, )


def test(command, threadcount, arg):
    greenlets = []
    for idx in range(threadcount):
        g = MyNoopGreenlet(idx, command, arg)
        greenlets.append(g)
        g.start()
    for g in greenlets:
        g.join()
    for idx, g in enumerate(greenlets):
        value = g.get()
        print '%d. value: %s' % (idx, value, )


def main():
    args = sys.argv[1:]
    try:
        opts, args = getopt.getopt(args, 'hc:t:', [
            '--help', '--command', '--threads', ])
    except:
        sys.exit(__doc__)
    command = None
    threadcount = 5
    for opt, val in opts:
        if opt in ('-h', '--help'):
            sys.stderr.write(__doc__)
            sys.exit(-1)
        elif opt in ('-c', '--command'):
            command = val
        elif opt in ('-t', '--threads'):
            threadcount = int(val)
    if command is None or len(args) != 1:
        sys.exit(__doc__)
    test(command, threadcount, args[0])

if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
