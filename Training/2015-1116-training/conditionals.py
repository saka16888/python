''' Goal:  Create the world's most brief set of notes and quick reference
           for tools useful for expressing tests elegantly
'''

__author__ = 'mihung'

import re

score = 75
dead_ports = {12, 8, 15, 25}
ports_in_use = {10, 14, 6, 7, 20}
allowed_ports = {2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 22}

def is_even(x):
    'Predicate returns true if x is even'
    return x % 2 == 0

print('pass' if score >= 70 else 'fail')                            # ternary operator or conditional expression
assert 0 <= score <= 100                                            # chained comparisons
assert score > 50 and not is_even(score)                            # short-circuit "and"
assert isinstance(score, int) or score > 1000                       # short-circuit "or"
assert score in {55, 65, 75, 85, 95}                                # fast membership test
assert 'brief' in __doc__                                           # substring test (but beware aliasing)
assert 'brief' in __doc__.split()                                   # list membership looks for an EXACT match
assert re.search(r'[Bb]rief', __doc__)                              # passes if "Brief" or "brief" is present

# Objective:  Make sure that none of the ports in use are dead
# Version 1 (worst way)
overlap = False
for port in ports_in_use:
    if port in dead_ports:
        overlap = True
assert not overlap

# Version 2
assert not any([port in dead_ports for port in ports_in_use])

# Version 3
assert not any(port in dead_ports for port in ports_in_use)

# Version 4
assert not ports_in_use.intersection(dead_ports)

# Version 5 (best way):  Highest level concept, "disjoint" and runs a C speed and has an early-out
assert ports_in_use.isdisjoint(dead_ports)

# Objective:  Make sure at lest one of the ports in use are even numbered ##################################
assert sum([is_even(port) for port in ports_in_use]) >= 1
assert any([is_even(port) for port in ports_in_use])
assert any(is_even(port) for port in ports_in_use)
assert any(map(is_even, ports_in_use))                       # <== Sometimes map() is best (fastest and most readable)


# Objective:  Make sure all the ports in use are numbered under 1024  ######################################
assert all([port < 1024 for port in ports_in_use])
assert all(port < 1024 for port in ports_in_use)             # <== Sometimes the genexp is more readable than a lambda
assert all(map(lambda port: port < 1024, ports_in_use))


# Objective:  Verify that all the ports in use are allowed ports ###########################################
assert all(port in allowed_ports for port in ports_in_use)
assert ports_in_use <= allowed_ports                         # <== Fastest clearest way is the subset test