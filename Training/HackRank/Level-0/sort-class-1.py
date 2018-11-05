from operator import itemgetter, attrgetter

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))

st = [
    Student("A", 2, 12),
    Student("B", 5, 15),
    Student("C", 3, 11),
    Student("D", 5, 11),
]
print("sorted(st) = ", sorted(st, key=attrgetter('name')))
print("sorted(st) = ", sorted(st, key=attrgetter('grade', 'name')))
print("sorted(st) = ", sorted(st, key=attrgetter('age')))
# print("sorted(st) = ",sorted(st,key=itemgetter('name'))) ; # error

# for n,g,a in sorted(st,key=itemgetter("name")):
# print("name=%s,grade=%d,age=%d" % (n,g,a))
# print("sorted(st)",sorted(st,key=itemgetter('name')))

student_tuples = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10), ]
print("sorted(student_tuples) = ", sorted(student_tuples, key=lambda stu: stu[2]))
print("sorted(student_tuples) = ", sorted(student_tuples, key=itemgetter(1)))