#!/usr/bin/env python

"""
Sample classes that support addition of points and calculation of vectors.
"""

import math


class Point(object):
    """A basic Cartesian point that knows its position in space
    (abscissa and ordinate).
    """
    def __init__(self, x=0.0, y=0.0):
        self._x = x
        self._y = y

    def _get_x(self):
        return self._x

    def _set_x(self, x):
        self._x = x
    x = property(_get_x, _set_x, doc='The abscissa (x coordinate) of a Point')

    def _get_y(self):
        return self._y

    def _set_y(self, y):
        self._x = y
    y = property(_get_y, _set_y, doc='The ordinate (y coordinate) of a Point')


class CalculatingPoint(Point):
    """A point that can calculate the sum and difference between itself
    and another point.
    """
    def vector(self, point):
        magnitude = 0
        direction = 0
        return magnitude, direction

    def add(self, point):
        x1 = self.x
        y1 = self.y
        x2 = point.get_x()
        y2 = point.get_y()
        x3 = x1 + x2
        y3 = y1 + y2
        return Point(x3, y3)
    __add__ = add

    def distance(self, point):
        x1 = self.x
        y1 = self.y
        x2 = point.x
        y2 = point.y
        distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
        return distance
    __sub__ = distance


def test1():
    p1 = CalculatingPoint(10.0, 10.0)
    p2 = CalculatingPoint(20.0, 20.0)
    print 'distance: %8.3f' % (p1.distance(p2), )
    print 'distance: %f' % (p1 - p2, )
    p2.x = 30
    p2.y = 40
    print 'distance: %f' % (p1 - p2, )


def test():
    test1()

if __name__ == '__main__':
    test()
