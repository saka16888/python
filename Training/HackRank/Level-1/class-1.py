class Basic:
    def __init__(self,name):
        self.name=name

    def show(self):
        print('This is Basic class"')

class Special(Basic):
    def __init__(self,name,edible):
        Basic.__init__(self,name)
        self.upper=name.upper()
        self.edible=edible
    def show(self):
        Basic.show(self)
        print("Special - upper name",self.upper)
        if self.edible:
            print("It's edible")
        else:
            print ("It's not edible")
    def edible(self):
        return self.edible
    objectname = property (show,edible)

b=Basic('Win')
b.show()
print('-' * 30)
s=Special('Game',1)
s.show()
# s.objectname = "Hello"


