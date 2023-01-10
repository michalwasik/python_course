""" Task 1 part 1
Create a Car class with two instance attributes:

.color, which stores the name of the car’s color as a string
.mileage, which stores the number of miles on the car as an integer
Then instantiate two Car objects—a blue car with 20,000 miles and a red car with 30,000 miles—and print out their
colors and mileage. Your output should look like this:

The blue car has 20000 miles.
The red car has 30000 miles.
"""


""" Task 1 part 2
Add class attribute .brand to the class and set it to your favourite car brand
"""


""" Task 1 part 3
Add instance attribute .convertible and set it default value to False, 
raise ValueError when user tries to set it to not boolean value

In [67]: Car('blue', 10_000, convertible=1)

ValueError: convertible attribute has to be True or False, got <class 'int'>
"""


""" Task 1 part 4
Add optional attribute .previous_owners which would be 
list of names of people that previously owner this vehicle

In [77]: car_1 = Car('blue', 10_000)

In [78]: car_2 = Car('red', 10_000)

In [79]: car_1.previous_owners.append('Filip')

In [80]: car_1.previous_owners
Out[80]: ['Filip']

In [81]: car_2.previous_owners
Out[81]: []
"""


""" Task 1 part 5
Create instance method .drove_more that will accept one positional argument which should be another instance of Car
that will return True if car given as argument has less miles driven, False otherwise
"""


""" Task 2
Create Rectangle class created with two tuples as arguments. These tuples contain the x and y coordinates 
of the upper left corner and the lower right corner. 
The constructor calculates the height and width of the rectangle based on these values.

Implement methods area and perimeter that calculate the area and perimeter of the rectangle based on 
the height and width. Create method move that moves the rectangle by the x and y values given as arguments.

The rectangle is represented in a coordinate system where the x coordinates increase from left to right, 
and the y coordinates increase from top to bottom. This is a common way of handling coordinates in programming because 
it is often easier and more natural to consider the top left corner of the computer screen as the point 
where x and y equal zero.

Implemented Rectangle class should pass following tests:

rectangle = Rectangle((1, 1), (4, 3))
print(rectangle.left_upper)  # -> (1, 1)
print(rectangle.right_lower)  # -> (4, 3)
print(rectangle.width)  # -> 3
print(rectangle.height)  # -> 2
print(rectangle.perimeter())  # -> 10
print(rectangle.area())  # -> 6
print(rectangle)  # -> will print `Rectangle (1, 1) ... (4, 3)`

rectangle.move(3, 3)
print(rectangle.left_upper)  # -> (4, 4)
print(rectangle.right_lower)  # -> (7, 6)
print(rectangle)  # -> will print `Rectangle (4, 4) ... (7, 6)`
"""


""" Task 3 part 1
Given base class
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

Please add to the class definition so that it works as follows:
watch = Stopwatch()
for i in range(3600):
    print(watch)
    watch.tick()
# ->
00:00
00:01
00:02
... many more lines printed out
00:59
01:00
01:01
... many, many more lines printed out
59:58
59:59
00:00
00:01
"""


""" Task 3 part 2
Please define a new class named Clock which expands on the capabilities of your Stopwatch class. 
It should work as follows:
clock = Clock(23, 59, 55)
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)

clock.set(12, 5)
print(clock)
# ->
23:59:55
23:59:56
23:59:57
23:59:58
23:59:59
00:00:00
00:00:01
12:05:00

As you can see above, the constructor should take initial values for the hours, minutes and seconds as arguments, 
and set these appropriately. The tick method adds one second to the clock. 
The set method sets new values for the hours and the minutes, and sets the seconds to zero.
"""


""" Task 4
Implement TaskList class, 
add method add_task that adds a new task to the self.tasks list. Each task also has a priority attached, 
which is used for sorting the tasks. The method get_next removes and returns the task with the highest priority 
on the list. There is also the number_of_tasks method, which returns the number of tasks on the list, 
and finally the method clear_tasks, which clears the task list.

Within the object, the tasks are stored in a list. Each task is of a tuple containing the priority of the task 
and its name. The priority value is stored first, so that when the list is sorted, the task with the highest priority 
is the last item on the list.
 This is why we can then simply use the pop method to retrieve and remove the highest priority item.

Please have a look at the following program with the task list in action:

tasks = TaskList()
tasks.add_task("studying", 50)
tasks.add_task("exercise", 60)
tasks.add_task("cleaning", 10)
print(tasks.number_of_tasks())  # -> 3
print(tasks.get_next())  # -> exercise
print(tasks.number_of_tasks())  # -> 2
tasks.add_task("date", 100)
print(tasks.number_of_tasks())  # -> 3
print(tasks.get_next())  # -> date
print(tasks.get_next())  # -> studying
print(tasks.number_of_tasks())  # -> 1
tasks.clear_tasks()
print(tasks.number_of_tasks())  # -> 0
"""


""" Task 5
Create class Person, that has 3 instance attributes title, name, surname and one class attribute 
TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')
in __init__, if given title is not one of TITLES, raise ValueError
"""


""" Task 6
Transform below code:


def calculate_gpa(grade_dict):
    return sum(grade_dict.values())/len(grade_dict)


students = {}
# We can set the keys to variables, so we might minimize typos
name, age, gender, level, grades = "name", "age", "gender", "level", "grades"
john, jane = "john", "jane"
math = "math"
students[john] = {}
students[john][age] = 12
students[john][gender] = "male"
students[john][level] = 6
students[john][grades] = {math:3.3}

students[jane] = {}
students[jane][age] = 12
students[jane][gender] = "female"
students[jane][level] = 6
students[jane][grades] = {math:3.5}

# At this point, we need to remember who the students are and where the grades are stored. 
# Not a huge deal, but avoided by OOP.
print(calculate_gpa(students[john][grades]))
print(calculate_gpa(students[jane][grades]))


# so that you'll be able to create and describe data using

# Define some students
john = Student("John", 12, "male", 6, {"math":3.3})
jane = Student("Jane", 12, "female", 6, {"math":3.5})

# Now we can get to the grades easily
print(john.getGPA())
print(jane.getGPA())
"""
