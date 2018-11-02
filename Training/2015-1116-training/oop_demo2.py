__author__ = 'mihung'

'''Goal:  Teach how OOP works in Python and how it used in PyATS.

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


Dunder Methods and their Shortcuts
----------------------------------

  ==========================    =============================    =================
  Operator/Keyword/Function     Dunder Method                    Description
  ==========================    =============================    =================
  len(s)                        s.__len__()                      sizeable
  pow(a, b) or a ** b           a.__pow__(b)
  s + t                         s.__add__(t)
  s * t                         s.__mul__(t)
  s % t                         s.__mod__(t)
  s in t                        t.__contains__(s)
  s[t]                          s.__getitem__(t)                 indexable
  s(a, b)                       s.__call__(a, b)                 callable
  for x in s:                   s.__getitem__() s.__iter__()     iterable
  print(s)                      s.__str__()
  ``>>> s``                     s.__repr__()
  with s:                       s.__enter__() s.__exit__()       context manager
  ==========================    =============================    =================


Principles and Terminology
--------------------------
Principles and Terminology
--------------------------

Inheritance
    One class decides to re-use code from another class.
    Inheritance is *completely* optional -- you can always
    live without by flattening the hierarchy.

Polymorphism
    Using the same method name in different classes to improve
    learnability and to save us from big if-elif-chains.

Introspection
    Asking an object what it capabitities are.
    This improves learnability and debuggability.
    This is how dir() and help() works.  It is also the
    key to how the test runner works in PyATS and py.test.

Mix-in Class
    A class that doesn't work by itself.  It just provides
    inherited capabilities to other classes.

Framework Design Pattern
    One of the *many* ways to use object orientd programming.
    The idea is that the parent class has the *business logic*
    and child class does has the actual *implementation details*.

Abstract Base Class
    A technique for giving discipline to mix-in classes.
    Mark the required underlying methods as "abstract methods".
    That puts those methods on a "todo list".  Then we inherit
    from ABC which checks to make sure the todo list is actually
    done before instantiates.
'''

class Animal:
    'A generic animal class'

    kind = 'critter'
    def __init__(self, name):
        self.name = name
    def tricks(self):
        print('\n%s is doing tricks' % self.name)
        self.talk()
        self.rollover()

    def talk(self):
        pass

    def rollover(self):
        pass


class Jumper:
    'A mix class for proving jump capabilities'

    def jump(self):
        print('Whee!  %s is jumping' % self.name)

class Cat(Animal, Jumper):
    'A simple feline class'

    kind = 'feline'

    def talk(self):
        print('Meow!  %s is purring' % self.name)

    def rollover(self):
        print('%s is rolling over playfully' % self.name)

class Dog(Animal, Jumper):
    'A simple canine class'

    kind = 'canine'

    def talk(self):
        print('Woof!  %s is barking' % self.name)

    def rollover(self):
        print('%s is rolling over' % self.name)

    def __len__(self):
        return len(self.name)

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError('Index out of range')
        return index * 111


##############################################################

if __name__ == '__main__':
    c = Cat('Socks')
    d = Dog('Fido')
    e = Dog('Buddy')
    f = Dog('Checkers')

    pets = [c, d, e, f]
    for pet in pets:
        pet.talk()

print('-' * 60)
print(dir(e))
print(e.name)
print(e.__dict__['name'])

a= Animal('Rex')
print(a.name)
a.talk()
a.rollover()

print('-' * 60)
a.tricks()
c.tricks()
d.tricks()
