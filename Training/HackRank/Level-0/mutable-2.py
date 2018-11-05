def my_function(param=[]):
    param.append("thing")
    return param

'''
What you might think would happen is that by giving an empty list as a default value to param,
a new empty list is allocated each time the function is called and no list is passed in.
But what actually happens is that every call that uses the default list will be using the same list.
This is because Python
(a) only evaluates functions definitions once,
(b) evaluates default arguments as part of the function definition, and
(c) allocates one list (a mutable object) for every call of that function.
See the following example:
'''

print(my_function())  # prints: ["thing"]
print(my_function())  # prints: ["thing", "thing"]

def my_function2(param):
    param.append("thing")
    return param

print(my_function2(["hello"]))  # prints: ["thing"]
print(my_function2(["hi"]))  # prints: ["thing", "thing"]

'''
Do not put a mutable object as the default value of a function parameter.
Immutable types are perfectly safe.
If you want to get the intended effect, do this.
'''

def my_function2(param=None):
    if param is None:
        param = []
    param.append("thing")
    return param
print(my_function2())  # prints: ["thing"]
print(my_function2())  # prints: ["thing"]
