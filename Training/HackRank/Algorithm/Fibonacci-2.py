# f(n)=f(n-2)+f(n-1)
def fib(n):
    if (n==0) or (n==1):
        print('n =%i, fib =%i ' % (n, n))
        return n
    elif (n<0):
        return
    a,b=0,1
    for i in range(n+1):
        print(i,a)
        tmp=a
        a,b=b,a+b
    print('fib(%i) =%i '% (n,tmp))

fib(-1)
fib(0)
fib(1)
fib(2)
fib(10)
fib(100)

