class Employee:
    'Common base class for all employees'
    ''' An object's attributes may or may not be visible outside the class definition.
        You need to name attributes with a double underscore prefix,
        and those attributes then are not be directly visible to outsiders.
        '''
    __empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.__empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.__empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
emp1.displayCount()
# print("Total Employee %d" % Employee.__empCount) #error, cannot access __empCount

emp1.age = 7  # Add an 'age' attribute.
emp1.age = 8  # Modify 'age' attribute.
# del emp1.age  # Delete 'age' attribute.

print(hasattr(emp1, 'age'))    # Returns true if 'age' attribute exists
print(getattr(emp1, 'age'))    # Returns value of 'age' attribute
print(setattr(emp1, 'age', 8)) # Set attribute 'age' at 8
print(dir(Employee))
# delattr(empl, 'age')    # Delete attribute 'age'
