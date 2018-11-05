class Demo:
    def __init__(self, i):
        self.i = i
        self.x = "xxx"
        self.y = "yyy"
        self.z = "zzz"

    def __str__(self):
        return str (self.i)

    def hello(self):
        print ("hello " + self.__str__ ())


d = Demo (22)
print (getattr (d, "__init__"))
print (getattr (d, "i"))
print (getattr (d, "x"))
print (getattr (d, "y"))
print (getattr (d, "z"))
print (getattr (d, "__str__"))
print (getattr (d, "hello"))
