#!/usr/bin/env python

"""
Sample classes that support addition of points and calculation of vectors.
"""

import math

NO_COLOR, RED, GREEN, BLUE = range(4)
STR_COLOR_MAP = {
    NO_COLOR: 'white',
    RED: 'red',
    GREEN: 'green',
    BLUE: 'blue',
    }


class Point(object):
    """A basic Cartesian point that knows its position in space
    (abscissa and ordinate).
    """
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.x = y


class RGBPoint(Point):
    """A point that knows its color and can describe itself.
    """
    def __init__(self, x=0.0, y=0.0, color=NO_COLOR):
        Point.__init__(self, x, y)
        self.color = color

    def describe(self):
        str_color = STR_COLOR_MAP[self.color]
        return 'x: %8.2f  y: %8.2f  color: %s' % (self.x, self.y, str_color, )


class CalculatingPoint(RGBPoint):
    """A point that can calculate the sum and difference between itself
    and another point.
    """
    def vector(self, point):
        magnitude = 0
        direction = 0
        return magnitude, direction

    def sum(self, point):
        """Return the sum of this Point and another Point.
        """
        x1 = self.x
        y1 = self.y
        x2 = point.get_x()
        y2 = point.get_y()
        x3 = x1 + x2
        y3 = y1 + y2
        return Point(x3, y3)
    __add__ = sum

    def difference(self, point):
        """Return the difference of this Point and another Point.
        """
        x1 = self.x
        y1 = self.y
        x2 = point.x
        y2 = point.y
        distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
        return distance
    __sub__ = difference


def test():
    p1 = CalculatingPoint(10.0, 10.0)
    p2 = CalculatingPoint(20.0, 20.0)
    print 'distance: %8.3f' % (p1.difference(p2), )
    print 'distance: %f' % (p1 - p2, )
    p2.set_x(30)
    p2.set_y(40)
    print 'distance: %f' % (p1 - p2, )
    cp1 = RGBPoint(5.0, 8.0, RED)
    print cp1.describe()


if __name__ == '__main__':
    test()
