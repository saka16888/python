#!/usr/bin/env python
"""
Solutions to the exercises for implementing classes.
"""

import math


class Point(object):
    """A Point class that maintains x and y coordinates.
    """
    def __init__(self, x, y):
        """Initialize the Point.  Save x and y."""
        self.x = x
        self.y = y

    def show(self):
        """Show the point."""
        print 'Point -- x: %s  y: %s  distance: %.4f' % (
            self.x, self.y, self.from_origin(), )

    def from_origin(self):
        """Calculate and return distance from origin."""
        distance = math.sqrt(self.x ** 2 + self.y ** 2)
        return distance


class DescriptionPoint(Point):
    """A Point class that also contains a description.

    Extends class Point.
    """
    def __init__(self, x, y, description):
        """Initialize the Point.  Save x and y and description."""
        super(DescriptionPoint, self).__init__(x, y)
        self.description = description

    def show(self):
        """Show the point."""
        #super(DescriptionPoint, self).show()
        #Point.show(self)
        distance = self.from_origin()
        print 'DescriptionPoint -- description: "%s"' % (
            self.description, )
        print '    x: %s  y: %s  distance: %.4f' % (
            self.x, self.y, distance, )


class ColorPoint(Point):
    """A Point class that also contains a color.

    Extends class Point.
    """
    def __init__(self, x, y, color):
        """Initialize the Point.  Save x and y and description."""
        super(ColorPoint, self).__init__(x, y)
        self.color = color

    def show(self):
        """Show the point."""
        distance = self.from_origin()
        print 'ColorPoint -- color: "%s"' % (
            self.color, )
        print '    x: %s  y: %s  distance: %.4f' % (
            self.x, self.y, distance, )


class ColorPoint2(Point):
    """A Point class that also contains a color.

    Extends class Point.

    Implements property for read/write access to color instance variable.

    """
    def __init__(self, x, y, color):
        """Initialize the Point.  Save x and y and description."""
        super(ColorPoint2, self).__init__(x, y)
        self._color = color

    def _get_color(self):
        print 'getting color'
        return self._color

    def _set_color(self, color):
        print 'setting color'
        self._color = color

    color = property(_get_color, _set_color)

    def show(self):
        """Show the point."""
        #super(DescriptionPoint, self).show()
        distance = self.from_origin()
        print 'ColorPoint -- color: "%s"' % (
            self._color, )
        print '    x: %s  y: %s  distance: %.4f' % (
            self.x, self.y, distance, )


class Wrapper(object):
    """A wrapper class that implements the context manager protocol.

    When used in a with: statement, this class prints a message
    before and after running the nested block.
    """
    def __enter__(self):
        print '>> Entering block'
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print '<< Exiting block'
        print 'exc_type:', exc_type
        # Return True in order to suppress the exception.
        return False

    def display(self, msg):
        print '|| %s ||' % (msg, )


def test():
    p1 = Point(25, 35)
    p2 = DescriptionPoint(45, 55, "an interesting point")
    p3 = ColorPoint(62, 49, 'red')
    points = [p1, p2, p3, ]
    for point in points:
        point.show()
    p4 = ColorPoint2(12, 15, 'green')
    p4.show()
    color = p4.color
    print 'color:', color
    p4.color = 'blue'
    p4.show()
    print '-' * 60
    with Wrapper() as obj:
        obj.display('In the block #1')
    print '-' * 60
    with Wrapper() as obj:
        obj.display('In the block #2-a -- you should see this.')
        raise RuntimeError('error in the "with" statement')
        obj.display('In the block #2-b -- you should *not* see this.')


if __name__ == '__main__':
    # dbg
    #import pdb; pdb.set_trace()
    test()
