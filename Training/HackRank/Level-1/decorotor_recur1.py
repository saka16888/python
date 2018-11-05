import time

def timing(f):
    def wrapper(*args):
       t1 = time.clock();
       #r = apply(f,args)
       t2 = time.clock();
       r=t2-t1
       print("%f seconds" % (t2-t1))
       return r
    return wrapper

@timing
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

r = fibonacci(5)
print("Fibonacci of %d is %d" % (5, r))
