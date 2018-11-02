__author__ = 'mihung'


''' Show how powerful list comprehensions are for testing and data analysis
    but only if you separate the three steps:

        #1 Acquire Data
        #2 Convert to a convenient form
        #3 Write a simple test or analyze the data

    Syntax for a list comprehension:
        [ <expr> for <var> in <iterable> if <cond> ]

    Syntax for a set comprehension:
        { <expr> for <var> in <iterable> if <cond> }

    Syntax for a dict comprehension:
        { <key_expr> : <value_expr> for <var> in <iterable> if <cond> }

    Syntax for a generator expression:
        ( <expr> for <var> in <iterable> if <cond> )

    General Rule:  Use genexps whenever you consume the data right away.
    If you need the values later, then use a list comprehension.

'''

import portfolio
from pprint import pprint

port = portfolio.get_portfolio('notes/stocks.txt')
pprint(port)

print('Projections == Looking at a subset of the columns')
print([trade.symbol for trade in port])
print([trade.shares for trade in port])
print([trade.price for trade in port])
print()

print('How many shares of Cisco have you purchased cumulatively?')
print('SELECT SUM(shares) FROM Port WHERE symbol = "CSCO";')
print(sum(trade.shares for trade in port if trade.symbol == 'CSCO'))
print()

print('Make an alphabetical list of the companies you have traded')
print('SELECT DISTINCT symbol FROM Port ORDER BY symbol;')
print(sorted({trade.symbol for trade in port}))
print()

print('How much have you invested cumulatively?')
print('SELECT SUM(shares * price) FROM Port;')
print(sum(tr.shares * tr.price for tr in port))

