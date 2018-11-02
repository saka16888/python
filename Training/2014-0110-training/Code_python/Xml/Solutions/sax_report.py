#!/usr/bin/env python

"""
Parse an XML document with SAX.  Display info about each element.

Usage:
    python sax_report.py infilename
Examples:
    python sax_report.py people.xml
"""


import sys
from xml.sax import make_parser, handler


class TestHandler(handler.ContentHandler):
    def __init__(self):
        self.level = 0
        self.document_node = None
        self.current_node = None

    def get_document_node(self):
        return self._document_node
    def set_document_node(self, document_node):
        self._document_node = document_node
    document_node = property(get_document_node, set_document_node)

    def show_with_level(self, value):
        print '%s%s' % ('    ' * self.level, value, )

    def startDocument(self):
        self.show_with_level('Document start')
        self.level += 1
        self.document_node = PeopleNode('document_root', {'name': 'test1'})
        self.current_node = self.document_node

    def endDocument(self):
        self.level -= 1
        self.show_with_level('Document end')

    def startElement(self, name, attrs):
        self.show_with_level('start element -- name: "%s"' % (name, ))
        self.level += 1
        node = PeopleNode()
        node.tag = name
        node.attrs = attrs
        node.parent = self.current_node
        self.current_node.children.append(node)
        self.current_node = node

    def endElement(self, name):
        self.level -= 1
        self.show_with_level('end element -- name: "%s"' % (name, ))
        self.current_node = self.current_node.parent

    def characters(self, content):
        content = content.strip()
        if content:
            self.show_with_level('characters: "%s"' % (content, ))
            self.current_node.charContent += content


class PeopleNode(object):
    def __init__(self, tag='[emptytag]', attrs=None, charContent='', children=None):
        self._tag = tag
        if attrs is None:
            self._attrs = {}
        else:
            self._attrs = attrs
        self.charContent = charContent
        if children is None:
            self.children = []
        else:
            self.children = children
        self._parent = None
    def get_tag(self):
        return self._tag
    def set_tag(self, tag):
        self._tag = tag
    tag = property(get_tag, set_tag)
    def get_attrs(self):
        return self._attrs
    def set_attrs(self, attrs):
        self._attrs = attrs
    attrs = property(get_attrs, set_attrs)
    def get_children(self):
        return self._children
    def set_children(self, children):
        self._children = children
    children = property(get_children, set_children)
    def get_parent(self):
        return self._parent
    def set_parent(self, parent):
        self._parent = parent
    parent = property(get_parent, set_parent)

    def show(self, level=0):
        #items = ', '.join(self.attrs.keys())
        print self.attrs.items()
        items = ['%s: "%s"' % (k, v,) for k, v in self.attrs.items()]
        items = ', '.join(items)
        print '%s%s -- %s' % ('    ' * level, self.tag, items, )
        level += 1
        for child in self.children:
            child.show(level)


def test(infilename):
    parser = make_parser()
    handler = TestHandler()
    parser.setContentHandler(handler)
    parser.parse(infilename)
    root_node = handler.document_node
    root_node.show()


def usage():
    print __doc__
    sys.exit(1)

def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    test(infilename)


if __name__ == '__main__':
    main()

