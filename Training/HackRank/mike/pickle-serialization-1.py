"""
This is test
https://docs.python.org/3/library/pickle.html
"""
import pickle
class  Person:
    def  __init__( self ,n,a):
        self.name=n
        self.age=a
    def  show( self ):
        print(self.name+ "_" +str( self.age))
a1 = Person("James",2)
a1.show()
a2 = Person("Hellen",15)
a2.show()
a_dict = {'da': 111, 2: [23,1,4], '23': {1:2,'d':'sad'}}

with open('pickle.txt','wb') as f:
    pickle.dump(a1,f,0)
    pickle.dump(a2, f, 0)
    pickle.dump(a_dict, f, 0)

with open('pickle.txt','rb') as f:
    b1=pickle.load(f)
    b1.show()
    b2 = pickle.load(f)
    b2.show()
    b3 = pickle.load(f)
    print(b3)

help('pickle-serialization-1')