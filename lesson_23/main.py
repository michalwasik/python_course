"""
Encapsulation
The most important principle of object orientation is encapsulation:
the idea that data inside the object should only be accessed
through a public interface – that is, the object’s methods.

Encapsulation is a good idea for several reasons:

* the functionality is defined in one place and not in multiple places.
* it is defined in a logical place – the place where the data is kept.
* data inside our object is not modified unexpectedly by external code in a completely
  different part of our program.
* when we use a method, we only need to know what result the method will
  produce – we don’t need to know details about the object’s internals in order to use it.
  We could switch to using another object which is completely different on the inside,
  and not have to change any code because both objects have the same interface.
"""

# Composition:


class StudentAddress:
    def __init__(self, student, city, street, number):
        self.student = student
        self.city = city
        self.street = street
        self.number = number


class Student:
    def __init__(self, name, student_number, city, street, number):
        self.name = name
        self.student_number = student_number
        self.classes = []
        self.address = StudentAddress(self, city, street, number)

    def enrol(self, course_running):
        self.classes.append(course_running)
        course_running.add_student(self)


class Department:
    def __init__(self, name, department_code):
        self.name = name
        self.department_code = department_code
        self.courses = {}

    def add_course(self, description, course_code, credits):
        self.courses[course_code] = Course(description, course_code, credits, self)
        return self.courses[course_code]


class Course:
    def __init__(self, description, course_code, credits, department):
        self.description = description
        self.course_code = course_code
        self.credits = credits
        self.department = department
        self.department.add_course(self)

        self.runnings = []

    def add_running(self, year):
        self.runnings.append(CourseRunning(self, year))
        return self.runnings[-1]


class CourseRunning:
    def __init__(self, course, year):
        self.course = course
        self.year = year
        self.students = []

    def add_student(self, student):
        self.students.append(student)


# maths_dept = Department("Mathematics and Applied Mathematics", "MAM")
# mam1000w = maths_dept.add_course("Mathematics 1000", "MAM1000W", 1)
# mam1000w_2013 = mam1000w.add_running(2013)
#
# bob = Student("Bob", "Smith")
# bob.enrol(mam1000w_2013)

"""
We have defined several relationships between these classes:
1. `Student` <-> `CourseRunning` - this is a many-to-many relationship.
2. `Course` -> `Department` - course can only have a single department, this is a one-to-many relationship.
3. `CourseRunning` -> `Course` - it is also bidirectional (one-to-many).
4. `Student` - `StudentAddress` - one-to-one
"""

# Inheritance:


class Person:
    def __init__(self, name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number


class Student(Person):
    UNDERGRADUATE, POSTGRADUATE = range(2)

    def __init__(self, student_type, *args, **kwargs):
        self.student_type = student_type
        self.classes = []
        super().__init__(*args, **kwargs)

    def enrol(self, course):
        self.classes.append(course)


class StaffMember(Person):
    PERMANENT, TEMPORARY = range(2)

    def __init__(self, employment_type, *args, **kwargs):
        self.employment_type = employment_type
        super().__init__(*args, **kwargs)


class Lecturer(StaffMember):
    def __init__(self, *args, **kwargs):
        self.courses_taught = []
        super().__init__(*args, **kwargs)

    def assign_teaching(self, course):
        self.courses_taught.append(course)


a_postgrad_course = 'Course1'
jane = Student(Student.POSTGRADUATE, "Jane", "Smith", "SMTJNX045")
jane.enrol(a_postgrad_course)

an_undergrad_course = 'Course2'
bob = Lecturer(StaffMember.PERMANENT, "Bob", "Jones", "123456789")
bob.assign_teaching(an_undergrad_course)

# Mix-ins:


class Person:
    def __init__(self, name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number


class LearnerMixin:
    classes = []

    def enrol(self, course):
        self.classes.append(course)


class TeacherMixin:
    courses_taught = []

    def assign_teaching(self, course):
        self.courses_taught.append(course)


class Tutor(Person, LearnerMixin, TeacherMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# tutor = Tutor('Micha', 'Wasi', 4)
# print(tutor.courses_taught)


class Learner:
    def __init__(self):
        self.classes = []

    def enrol(self, course):
        self.classes.append(course)


class Teacher:
    def __init__(self):
        self.courses_taught = []

    def assign_teaching(self, course):
        self.courses_taught.append(course)


class Person:
    def __init__(self, name, surname, number, learner=None, teacher=None):
        self.name = name
        self.surname = surname
        self.number = number

        self.learner = learner
        self.teacher = teacher

    @property
    def is_learner(self) -> bool:
        return bool(self.learner)

    def set_learner(self, learner: 'Learner'):
        self.learner = learner


normal_numan = Person('Dawid', 'Góreczny', 1)
normal_numan.set_learner(Learner())
print(normal_numan.is_learner)
