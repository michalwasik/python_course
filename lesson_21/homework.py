# Task 1
class Car:
    brand = 'Ford'

    def __init__(self, color: str, mileage: int, convertible: bool = False, previous_owner=None) -> None:
        self.color = color
        self.mileage = mileage
        self.convertible = convertible
        if not previous_owner:
            self.previous_owner = []
        if not isinstance(convertible, bool):
            raise ValueError(f'convertible attribute has to be True or False, '
                             f'got {type(convertible)} instead')

    def drove_more(self, car): # how to type class instance arg?
        if car.mileage < self.mileage:
            return True
        else:
            return False


blue = Car('blue', 20000)
red = Car('red', 30000)
red.previous_owner.append('Filip')
# print(blue.previous_owner)
# print(red.previous_owner)
# print(blue.drove_more(red))

# after making previous_owner = [], and self.previous_owner = previous_owner, blue car had same owner as red?

# print(f'The {blue.color} {blue.brand} has {blue.mileage} miles.')
# print(f'The {red.color} {red.brand} has {red.mileage} miles.')

# Task 2


class Rectangle:

    def __init__(self, left_upper: tuple[int, int], right_lower: tuple[int, int]) -> None:
        self.left_upper = left_upper
        self.right_lower = right_lower
        self.height = right_lower[1] - left_upper[1]
        self.width = right_lower[0] - left_upper[0]

    def perimeter(self):
        return 2 * (self.height + self.width)

    def area(self):
        return self.width * self.height

    def move(self, x: int, y: int):
        self.right_lower = (self.right_lower[0] + x, self.right_lower[1] + y)
        self.left_upper = (self.left_upper[0] + x, self.left_upper[1] + y)

    def __str__(self):
        return f'Rectangle {self.left_upper} ... {self.right_lower}'


# rectangle = Rectangle((1, 1), (4, 3))
# print(rectangle.left_upper)  # -> (1, 1)
# print(rectangle.right_lower)  # -> (4, 3)
# print(rectangle.width)  # -> 3
# print(rectangle.height)  # -> 2
# print(rectangle.perimeter())  # -> 10
# print(rectangle.area())  # -> 6
# print(rectangle) # -> will print `Rectangle (1, 1) ... (4, 3)`
# rectangle.move(3, 3)     Q: czy da sie zwiekszyc wartosci w tupli jakos ładniej? :)
# print(rectangle.left_upper)  # -> (4, 4)
# print(rectangle.right_lower)  # -> (7, 6)
# print(rectangle)  # -> will print `Rectangle (4, 4) ... (7, 6)`

# Task 3
import datetime
from time import sleep


class Stopwatch:
    watch_format = "%M:%S"

    def __init__(self):
        self.seconds = 0
        self.minutes = 0
        self.rn_time = datetime.datetime(year=2020, month=1, day=1, minute=self.minutes, second=self.seconds)

    def __str__(self):
        return f'{self.rn_time.strftime(self.watch_format)}'

    def tick(self):
        self.rn_time += datetime.timedelta(seconds=1)
        sleep(1)


# watch = Stopwatch()
# for i in range(3600):
#     print(watch)
#     watch.tick()

class Clock(Stopwatch):
    watch_format = "%H:%M:%S"

    def __init__(self, hr, mins, sec):
        super().__init__()
        self.seconds = sec
        self.minutes = mins
        self.hours = hr
        self.rn_time = datetime.datetime(year=2020, month=1, day=1, hour=self.hours, minute=self.minutes,
                                         second=self.seconds)

    def __str__(self):
        return f'{self.rn_time.strftime(self.watch_format)}'

    def set(self, hr: int, mins: int = 0, sec: int = 0):
        self.rn_time = self.rn_time.replace(hour=hr, minute=mins, second=sec)


# clock = Clock(23, 59, 55)
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)
# clock.set(12, 5)
# print(clock)

# Task 4


class TaskList:
    tasks = []

    def add_task(self, activity: str, priority: int):
        self.tasks.append((activity, priority))
        self.tasks.sort(key=lambda x: x[1])

    def number_of_tasks(self):
        return len(self.tasks)

    def get_next(self):
        next_exe = self.tasks.pop(-1)
        return next_exe[0]

    def clear_tasks(self):
        self.tasks.clear()


# tasks = TaskList()
# tasks.add_task("studying", 50)
# tasks.add_task("exercise", 60)
# tasks.add_task("cleaning", 10)
# print(tasks.number_of_tasks())  # -> 3
# print(tasks.get_next())  # -> exercise
# print(tasks.number_of_tasks())  # -> 2
# tasks.add_task("date", 100)
# print(tasks.number_of_tasks())  # -> 3
# print(tasks.get_next())  # -> date
# print(tasks.get_next())  # -> studying
# print(tasks.number_of_tasks())  # -> 1
# tasks.clear_tasks()
# print(tasks.number_of_tasks())  # -> 0

# Task 5

class Person:
    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    def __init__(self, title: str, name: str, surname: str):
        self.title = title
        self.name = name
        self.surname = surname
        if self.title not in self.TITLES:
            raise ValueError()


# jeremy = Person('Dr', 'Jeremy', 'Clarc')
# jeremy = Person('Dupa', 'Jeremy', 'Clarc')

# Task 6


class Student:

    def __init__(self, name, age, gender, level, grades):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level
        self.grades = grades

    def getGPA(self) -> float:  # Function name should be lowercase ; p
        return sum(self.grades.values()) / len(self.grades)


john = Student("John", 12, "male", 6, {"math": 2.3, "bio": 5})
jane = Student("Jane", 12, "female", 6, {"math": 3.5, "polish": 1})

# print(john.getGPA())
# print(jane.getGPA())
