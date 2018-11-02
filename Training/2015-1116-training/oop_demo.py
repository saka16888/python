''' Goal:  Teach how OOP works in Python and how it used in PyATS

Underlying Structure
--------------------

* Classes hold **SHARED** information

  1) ``__name__`` a string with the name given at birth
  2) ``__bases__`` a tuple of parent (base) class for code re-use
  3) ``__dict__`` a dict holding all the shared information

* Instance hold **UNIQUE** information

  1) ``__class__`` reference to the class with the shared information
  2) ``__dict__`` a dict holding the unique information

Namespaces
----------

* globals:   ``__name__``, ``__doc__``, ``Dog``, ``d``, ``e``, ``f``
* Dog:       ``__name__``, ``__doc__``, ``kind``
* instance:  ``name``

'''

class Cat:
    'A simple feline class'

    kind = 'feline'

    def __init__(self, name):
        self.name = name

    def talk(cat):
        print('Meow!  %s is purring' % cat.name)

class Dog:
    'A simple canine class'

    kind = 'canine'

    def __init__(self, name):
        self.name = name

    def talk(dog):
        print('Woof!  %s is barking' % dog.name)

##############################################################

c = Cat('Socks')
d = Dog('Fido')
e = Dog('Buddy')
f = Dog('Checkers')

pets = [c, d, e, f]
for pet in pets:
    pet.talk()

print("dir(c) =", dir(c))
print(Cat.__dir__)
print(Cat.__class__)
print(Cat.__dict__)
print(Cat.__name__)

print(dir(e))
print(e.name)
print(e.__dict__['name'])
