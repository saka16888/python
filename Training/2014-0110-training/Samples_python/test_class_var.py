class A(object):

    Label = "Some string"

    def __init__(self, name):
        self.name = name


def test():
    a = A('alfred')
    b = A('billy')
    print(a.name)
    print(b.name)
    print(a.Label)
    print(b.Label)
    print(A.Label)


if __name__ == '__main__':
    test()
