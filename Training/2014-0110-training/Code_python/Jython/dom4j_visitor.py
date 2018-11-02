# -*- mode: pymode; coding: utf-8; -*-

"""
Use dom4j visitor pattern to walk elements/nodes in an XML document.

Print out a bit of information about each node.

Usage:
    jython dom4j_visitor.py myxmldoc.xml
"""

import sys
from org.dom4j.io import SAXReader
from org.dom4j import VisitorSupport
from org.dom4j.tree import DefaultElement, DefaultText, DefaultDocument


class Visitor(VisitorSupport):
    def __init__(self):
        VisitorSupport.__init__(self)
        self.count = 0
    def visit(self, el):
        self.count += 1
        #
        # Distinguish between various node types.
        # The type of a node can be learned by printing a string
        #   representation of the node or by inspecting el.__class__.
        if isinstance(el, DefaultElement):
            print 'Element %d. name: "%s"  text: "%s"  class: %s' % (
                self.count, el.getName(), el.getText(), el.__class__, )
        elif isinstance(el, DefaultText):
            print 'Text %d. text: "%s"  class: %s' % (
                self.count, el.getText(), el.__class__, )
        elif isinstance(el, DefaultDocument):
            print 'Document %d. text: "%s"  class: %s' % (
                self.count, el.getText(), el.__class__, )
        else:
            print 'Other %d. name: "%s"  text: "%s"  class: %s' % (
                self.count, el.getName(), el.getText(), el.__class__, )


def test(indocname):
    reader = SAXReader()
    doc = reader.read(indocname)
    visitor = Visitor()
    doc.accept(visitor)


def usage():
    print __doc__
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    indocname = args[0]
    test(indocname)


if __name__ == '__main__':
    main()
