#!/usr/bin/env python

"""Process an XML document with minidom.

Show the document tree.
Modify the document tree and then show it again.

Usage:
    python minidom_walk.py [options] infilename
Options:
    -h, --help      Display this help message.
Example:
    python minidom_walk.py myxmldoc.xml
"""


#
# Imports:
import sys
import getopt
import time
from xml.dom import minidom


#
# Functions for internal use:

def show_tree(doc, quiet=False):
    root = doc.documentElement
    show_node(root, 0, quiet)


def show_node(node, level, quiet=False):
    count = 0
    if node.nodeType == minidom.Node.ELEMENT_NODE:
        if not quiet:
            show_level(level)
            print 'tag: %s' % (node.nodeName, )
        for key in node.attributes.keys():
            attr = node.attributes.get(key)
            if not quiet:
                show_level(level + 1)
                print '- attribute name: %s  value: "%s"' % (
                    attr.name, attr.value, )
        if (len(node.childNodes) == 1 and
                node.childNodes[0].nodeType == minidom.Node.TEXT_NODE):
            if not quiet:
                show_level(level + 1)
                print '- data: "%s"' % (node.childNodes[0].data, )
        for child in node.childNodes:
            count += 1
            show_node(child, level + 1, quiet)
    return count


def show_level(level):
    for x in range(level):
        print '   ',


def modify_tree(doc, tag, attrname, attrvalue):
    root = doc.documentElement
    modify_node(root, tag, attrname, attrvalue)


def modify_node(node, tag, attrname, attrvalue):
    if node.nodeName == tag:
        node.setAttribute(attrname, attrvalue)
    for child in node.childNodes:
        modify_node(child, tag, attrname, attrvalue)


def test(docname):
    """Test the functions in this module.
    """
    doc = minidom.parse(docname)
    show_tree(doc)
    print '-' * 50
    date = time.ctime()
    modify_tree(doc, 'person', 'date', date)
    show_tree(doc)


USAGE_TEXT = __doc__


def usage():
    print USAGE_TEXT
    sys.exit(1)


def main():
    args = sys.argv[1:]
    try:
        opts, args = getopt.getopt(args, 'h', ['help', ])
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
