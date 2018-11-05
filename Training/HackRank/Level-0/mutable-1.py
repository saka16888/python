x=5.0
print("id(x) = ",id(x))
x += 7.0
print("id(x) = ",id(x))
print("Value ",x)

'''****************************'''
print('*' * 40)
x = 'foo'
y = x
print(x,y) # foo
print("id(x) = ",id(x))
print("id(y) = ",id(y))
y += 'bar'
print(x,y) # foo foobar
print("id(x) = ",id(x))
print("id(y) = ",id(y))

x += "hello "
print(x,y) # foohello  foobar
print("id(x) = ",id(x))
print("id(y) = ",id(y))

'''****************************'''
print('*' * 40)
x = [1, 2, 3]
y = x
print(x) # [1, 2, 3]
print("id(x) = ",id(x))
print("id(y) = ",id(y))
y += [3, 2, 1]
print(x, y) # [1, 2, 3, 3, 2, 1]
print("id(x) = ",id(x))
print("id(y) = ",id(y))

def func(val):
    val += 'bar'

x = 'foo'
print("x=",x) # foo
func(x)
print("after func(x) = ",x) # foo

def func(val):
    val += [3, 2, 1]

x = [1, 2, 3]
print(x) # [1, 2, 3]
func(x)
print("after func(x) = ",x) # [1, 2, 3, 3, 2, 1]

def f2(val):
    val[0]= 5

x = [1, 2, 3]
print(x) # [1, 2, 3]
f2(x)
print("after func(x) = ",x) # [1, 2, 3, 3, 2, 1]