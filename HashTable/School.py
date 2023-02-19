from HashTable.SeparateChainingHashtable import SeparateChainingHashtable


class Student:

    def __init__(self, student_id, firstname, surname):
        self.id = student_id
        self.firstname = firstname
        self.surname = surname
        self.grades = SeparateChainingHashtable()  # dict()

    # We used merely the id to compute a student's hash, under
    # the assumption that it is unique. We could have used more
    # fields of a Student object.
    def __hash__(self):
        return hash(self.id)

    def __repr__(self):  # must return a string
        return "<" + self.firstname + " " + self.surname + \
               ", Id= " + str(self.id) + ", Hash=" + str(hash(self)) + ">"
        # Python uses the
        # memory address of an object to compute the value of hash on it

    def update_grade(self, course, new_grade):
        self.grades[course] = new_grade

    def avg(self):
        s = sum([self.grades[course] for course in self.grades])
        return s / len(self.grades)

    def __eq__(self, other):
        return self.firstname == other.firstname and \
               self.surname == other.surname and \
               self.id == other.id


def app_driver():

    peter_pan = Student(1234, 'Peter', 'Pan')
    tinker_bell = Student(5678, 'Tinker', 'Bell')
    tiger_lily = Student(9123, 'Tiger', 'Lily')

    peter_pan.grades.put(hash('SDA'), 95)
    peter_pan.grades.put(hash('DS'), 89)
    peter_pan.grades.put(hash('OSX'), 74)

    print(peter_pan)
    print(peter_pan.grades.find(hash('SDA')))
    print(peter_pan.grades.find(hash('DS')))
    print(peter_pan.grades.find(hash('OSX')))

    print(peter_pan.avg())


app_driver()
