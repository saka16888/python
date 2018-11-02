'Acquire stock information and convert it to a convenient form'

import csv
from collections import namedtuple

Trade = namedtuple('Trade', ['symbol', 'shares', 'price'])

def get_portfolio(filename):
    '''Parse a comma delimited file of stock trades into a list of
       named tuples in form: [Trade(symbol, shares, price), ...]

    '''
    trades = []
    with open(filename) as f:
        for symbol, shares, price in csv.reader(f):
            trade = Trade(symbol, int(shares), float(price))
            trades.append(trade)
    return trades

if __name__ == '__main__':
    from pprint import pprint

    port = get_portfolio('notes/stocks.txt')
    pprint(port)