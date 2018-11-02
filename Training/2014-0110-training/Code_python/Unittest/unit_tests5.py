#!/usr/bin/env python

"""
unit_tests5.py

Sample unittest -- Create suite, then add individual tests (functions).
"""

import unittest
from xml.dom import minidom
import minidom_walk
import unit_tests_dbg


class MinidomTestCase(unittest.TestCase):

##     def __init__(self, documentname):
##         unittest.TestCase.__init__(self)
##         self.documentname = documentname

    def setUp(self):
        self.doc = minidom.parse('people.xml')

    def test_getroot(self):
        # Can we get the root element of the document?
        unit_tests_dbg.dbgprint('test #1')
        root = self.doc.documentElement
        self.assertTrue(isinstance(root, minidom.Element))

    def test_children(self):
        # Does the root element have at least one child element?
        unit_tests_dbg.dbgprint('test #2')
        root = self.doc.documentElement
        foundOne = False
        for child in root.childNodes:
            if child.nodeType == minidom.Node.ELEMENT_NODE:
                foundOne = True
                break
        self.assertTrue(foundOne)

    def test_minidomwalk(self):
        # Does show_node() process at least one child?
        unit_tests_dbg.dbgprint('test #3')
        root = self.doc.documentElement
        count = minidom_walk.show_node(root, 1, True)
        self.assertTrue(count > 0)


def get_suite():
    suite = unittest.TestSuite()
    suite.addTest(MinidomTestCase('test_getroot'))
    suite.addTest(MinidomTestCase('test_children'))
    return suite


def main():
    suite = get_suite()
    # verbosity = 0 (none) or 1 (dots) or 2 (name/description)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    #unittest.main()
    main()
