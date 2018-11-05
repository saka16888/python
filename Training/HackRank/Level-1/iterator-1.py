class A:
    def __init__(self):
        self.data = [11,22,33]
        self.idx = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.idx < len(self.data):
            x = self.data[self.idx]
            self.idx +=1
            return x
        else:
            raise StopIteration

class B:
    def __init__(self, n):
        self.i = 0
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()
def test():
    a=A()
    print('list(a) = ',list(a))
    print('list(a) = ',list(a))
    b = B(2)
    print('list(b) = ',list(b))
    b2=B(5)
    print('list(b2) = ',list(b2))
    # for x in list(a):
    #     print(x)
if __name__ == '__main__':
    test()

