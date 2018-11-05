import sys

N = int(input().strip())
# N=24
if (N % 2 == 1) :
    print('Weird')
elif (N >= 2 and N <= 5):
    print('Not Weird')
elif (N >= 6 and N <= 20):
    print('Weird')
elif (N >= 20 and N <= 100):
    print('Not Weird')
