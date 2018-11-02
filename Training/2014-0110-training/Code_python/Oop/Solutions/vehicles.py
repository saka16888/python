#!/usr/bin/env python


"""
Implementation of the Vehicle class hierarchy.

Usage:
    python vehicles.py [options] [arg ...]
Options:
    -h, --help      Display this help message.
    -v, --verbose   Verbose -- Print extra info.
Example:
    python vehicles.py
    python vehicles.py --verbose
"""


#
# Imports:
import sys
import getopt


#
# Global variables and constants:


#
# Functions for external use, factories, etc:


#
# Classes:

class Vehicle(object):
    """The root of the vehicle class hierarchy.
    """
    def __init__(self, id, fuel=0):
        self.id = id
        self.fuel = fuel

    def show(self):
        print 'ID: %s' % (self.id, )
        print '    fuel: %d' % (self.fuel, )


class Truck(Vehicle):
    def __init__(self, id, fuel=0, wheel_count=4):
        Vehicle.__init__(self, id, fuel)
        self.wheel_count = wheel_count

    def show(self):
        Vehicle.show(self)
        print '    wheel count: %d' % (self.wheel_count, )


class PickupTruck(Truck):
    pass


class BigRig(Truck):
    """An 18-wheeler.
    """
    def __init__(self, id, fuel=0, wheel_count=4, max_load=-1, current_load=0):
        Truck.__init__(self, id, fuel, wheel_count)
        self.max_load = max_load
        self.current_load = current_load

    def show(self):
        Truck.show(self)
        print '    max load: %d' % self.max_load
        print '    current load: %d' % self.current_load


class Automobile(Vehicle):
    pass


class Van(Automobile):
    """A passenger vehicle.  A small bus.
    """
    def __init__(self, id, fuel=0, stops=None):
        Automobile.__init__(self, id, fuel)
        if stops is None:
            self.stops = []
        else:
            self.stops = stops

    def show(self):
        Automobile.show(self)
        print '    stops -- total passenger count: %d:' % (
            self.calc_pickups(), )
        for stop in self.stops:
            print '        %s' % str(stop)

    def calc_pickups(self):
        count = 0
        for stop in self.stops:
            count += stop.get_passenger_count()
        return count


class Sedan(Automobile):
    pass


class PassengerStop(object):
    """A passenger stop or pickup.
    Remembers the location and the expected number of passengers.
    """
    def __init__(self, location, passenger_count):
        self.location = location
        self.passenger_count = passenger_count

    def __str__(self):
        return 'Passenger stop -- location: "%s"  passenger count: %d' % (
            self.location, self.passenger_count, )

    def get_passenger_count(self):
        return self.passenger_count

    def set_passenger_count(self, passenger_count):
        self.passenger_count = passenger_count

    def show(self):
        msg = 'Passenger stop -- location: "%s"  passenger count: %d' % (
            self.location, self.passenger_count, )
        print msg,


#
# Functions for internal use:

def test(verbose):
    """Test the Vehicle class hierarchy.
    Create some vehicles; put them in a "fleet"; show them.
    """
    bigrig1 = BigRig('a001', 100, 18, 20000, 10000)
    bigrig2 = BigRig('a002', 150, 18, 24000, 12000)
    stops = [
        PassengerStop('1st and Main', 3),
        PassengerStop('9th and J', 2),
        ]
    van1 = Van('b001', 40, stops)
    stops = [
        PassengerStop('888 Far Out Road', 2),
        PassengerStop('123 Twisted Way', 1),
        ]
    van2 = Van('b002', 40, stops)
    pickuptruck1 = PickupTruck('c001', 20)
    pickuptruck2 = PickupTruck('c002', 40, 6)
    fleet = [
        bigrig1,
        bigrig2,
        van1,
        van2,
        pickuptruck1,
        pickuptruck2,
        ]
    for vehicle in fleet:
        hr(verbose)
        vehicle.show()


def hr(verbose):
    if verbose:
        print '-' * 50


def usage():
    print __doc__
    sys.exit(1)


def main():
    args = sys.argv[1:]
    try:
        opts, args = getopt.getopt(args, 'hv', [
            'help', 'verbose',
            ])
    except:
        usage()
    verbose = False
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt in ('-v', '--verbose'):
            verbose = True
    if len(args) != 0:
        usage()
    test(verbose)


if __name__ == '__main__':
    #import pdb
    #pdb.set_trace()
    main()
