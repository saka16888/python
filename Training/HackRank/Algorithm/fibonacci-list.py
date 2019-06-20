def fib(n):
    tmp = []
    a,b = 0,1
    inc = -1 if n<0 else 1
    if n >=0:
        #print("inc = %d" % inc)
        for i in range(0,n+1,inc):
            tmp.append(a)
            a, b = b, a+b
    # else:
    #     for i in range(0,n+1,inc):
    #         tmp.append(a)
    #         a, b = b, a+b
    return tmp

print(fib(-1))
print(fib(0))
print(fib(1))
print(fib(2))
<<<<<<< HEAD:Training/HackRank/Algorithm/fibonacci-list.py
print(fib(8))
print(fib(256))
=======
print(fib(20))
>>>>>>> d047a4498263098e75c657701b835e59cd3f2ca1:Training/2015-1116-training/fibonacci.py

