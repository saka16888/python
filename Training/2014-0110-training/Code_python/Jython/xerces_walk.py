"""
Parse an XML document using the Xerces DOMParser.

Display node names and attributes.
"""


from org.apache.xerces.parsers import DOMParser as dp


def show_node(node, level):
    while node:
        if node.getNodeType() == node.ELEMENT_NODE:
            indent = show_level(level)
            print '%sname: %s' % (indent, node.getTagName(), )
            attrs = node.getAttributes()
            count = attrs.getLength()
            for idx in range(count):
                attr = attrs.item(idx)
                print '%s    %s: %s' % (
                    indent, attr.getNodeName(), attr.getNodeValue(),)
            child = node.getFirstChild()
            show_node(child, level + 1)
        node = node.getNextSibling()


def show_level(level):
    return '    ' * level


def test():
    parser = dp()
    parser.parse('people.xml')
    doc = parser.getDocument()
    node = doc.getFirstChild()
    node = node.getFirstChild()
    show_node(node, 0)


if __name__ == '__main__':
    test()


