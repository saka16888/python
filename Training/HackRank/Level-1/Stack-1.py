
class Stack():
    def __init__(self,n):
        self.data=[]
        self.data.extend(n)

    def pop(self):
        return self.data.pop()

    def push(self,n):
        self.data.extend(n)

    def printStack(self):
        print(self.data)

s1=Stack([3])
s1.push([4])
s1.printStack()
s1.push([6,7])
s1.printStack()
print(s1.pop())
s1.printStack()

'''
append adds its argument as a single element to the end of a list.
The length of the list itself will increase by one.
extend iterates over its argument adding each element to the list,
extending the list.
The length of the list will increase by
however many elements were in the iterable argument.
'''
x = [1, 2, 3]
x.append([4, 5])
print (x)

# Extends list by appending elements from the iterable.
x = [1, 2, 3]
x.extend([4, 5])
print (x)

x = [1, 2, 3]
x.extend("abc")
print (x)

x = [1, 2, 3]
x.insert(2,4)
print (x)



