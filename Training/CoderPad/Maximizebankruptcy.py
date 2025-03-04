'''
A finance company is carrying out a study on the worst stock investments and would like to acquire a program to do so.
The program must be able to analyze a chronological series of stock values in order to show the largest loss
that it is possible to make by buying a share at a given time and selling it at a later date.
The loss will be expressed as the difference between the two values.
If there is no loss, it will be considered 0.
You will receive a list as input, containing the stock values arranged in order,
from the date of their introduction to the last known value.
The values are integers.
You must return the maximal loss p, expressed negatively if there is a loss, otherwise 0.

The list can be of significant size (up to 100000 elements). Each value is an integer between 0 and 2^31.

Example
stock_prices = (3, 2, 4, 2, 1, 5)

The function must return -3.


'''


def print_matrix(matrix):
    for row in matrix:
        print(row)

def maxBankruptcy(stock):
    max_loss_p=0
    n=len(stock)
    loss = [[0 for j in range(n)] for i in range(n)]
    #loss = [[0 * n] for i in range(n)]
    print_matrix(loss)
    for i in range(n):
        for j in range(i+1,n):
            loss[j-1][j]=stock[j]-stock[j-1]
            loss[i][j]=loss[i][j-1]+loss[j-1][j]
            print(i,j)
            print_matrix(loss)
            max_loss_p = min(max_loss_p,loss[i][j])
    return max_loss_p


def max_loss(prices):
    if len(prices) < 2:
        return 0  # Not enough prices for a loss

    max_price = prices[0]
    max_loss = 0

    for price in prices[1:]:
        loss = price - max_price
        max_loss = min(max_loss, loss)  # We want the most negative loss
        max_price = max(max_price, price)  # Update max price seen so far
        print("price",price,"max_price",max_price,"max_loss",max_loss)
    return max_loss

stock_prices = (3, 2, 4, 2, 1, 5, 8, 6, 4)
print(maxBankruptcy(stock_prices))

print(max_loss(stock_prices))