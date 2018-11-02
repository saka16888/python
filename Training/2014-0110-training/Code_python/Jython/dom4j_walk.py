#!/usr/bin/env python

"""Process an XML document with dom4j.

Show the document tree.
Modify the document tree and then show it again.

Usage:
    python dom4j_walk.py [options] infilename
Options:
    -h, --help      Display this help message.
Example:
    python dom4j_walk.py myxmldoc.xml
"""


#
# Imports:
import sys
import getopt
import time
# from org.dom4j import Document, DocumentException
from org.dom4j.io import SAXReader

#
# Global variables and constants:



#
# Functions for external use, factories, etc:



#
# Classes:



#
# Functions for internal use:

def show_tree(doc, msg):
    print '-' * 50
    print msg
    root = doc.getRootElement()
    show_node(root, 0)


def show_node(node, level):
    if node.nodeType == node.ELEMENT_NODE:
        show_level(level)
        print 'tag: %s' % (node.getQName().getName(), )
        for attr in node.attributeIterator():
            show_level(level + 1)
            print '- attribute name: %s  value: "%s"' % (
                attr.getName(), attr.getValue(), )
        if len(node.elements()) == 0:
            show_level(level + 1)
            print '- data: "%s"' % (node.getText(), )
        for child in node.elementIterator():
            show_node(child, level + 1)


def show_level(level):
    for x in range(level):
        print '   ',


def modify_tree(doc, tag, attrname, attrvalue):
    root = doc.getRootElement()
    modify_node(root, tag, attrname, attrvalue)


def modify_node(node, tag, attrname, attrvalue):
    if node.getQName().getName() == tag:
        node.setAttributeValue(attrname, attrvalue)
    for child in node.elementIterator():
        modify_node(child, tag, attrname, attrvalue)


def modify_tree_xpath(doc, path, attrname, attrvalue):
    nodes = doc.selectNodes(path)
    for node in nodes:
        node.setAttributeValue(attrname, attrvalue)


def test(docname):
    """Test the functions in this module.
    """
    reader = SAXReader()
    doc = reader.read(docname)
    show_tree(doc, 'Original tree:')
    date = time.ctime()
    modify_tree(doc, 'person', 'date', date)
    show_tree(doc, 'After walk and modify:')
    modify_tree_xpath(doc, '//people/person/name', 'date', date)
    show_tree(doc, 'After XPath modify:')


USAGE_TEXT = __doc__

def usage():
    print USAGE_TEXT
    sys.exit(1)


def main():
    args = sys.argv[1:]
    try:
        opts, args = getopt.getopt(args, 'h', ['help',
            ])
    except:
        usage()
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
    if len(args) != 1:
        usage()
    docname = args[0]
    test(docname)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
