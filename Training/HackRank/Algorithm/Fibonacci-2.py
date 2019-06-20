# f(n)=f(n-1)+f(n-2)
def fib(n):
    if (n==0) or (n==1):
        # print('fib(%i) = %i ' % (n, n))
        return n
    elif (n<0):
        return
    n1,n2=0,1
    for i in range(2,n+1):
        #print(i,a1)
        n1, n2 = n2, n1 + n2
        fn=n2
    #print('fib(%i) = %i '% (n,fn))
    return(fn)

n=100
for i in range(0,n+1):
    print('fib(%d) = %d ' % (i, fib(i)))
# fib(-1)
# fib(0)
# fib(1)
# fib(2)
# fib(5)
# fib(100)

