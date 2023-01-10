""" Task 1
Rewrite the Person class so that a person’s age is calculated for the first time when a new person instance is created,
and recalculated (when it is requested) if the day has changed since the last time that it was calculated.

class Person:

    def __init__(self, birthdate: datetime.datetime):
        self.birthdate = birthdate
        self._age: int | None = None

    def age(self):
        if self._age:
            print('from cache')
            return self._age
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        self._age = age
        return self._age


# Should work like this:
In [6]: pency = Person(datetime(1999, 4, 15))

In [7]: pency.age()
Out[7]: 23

In [8]: pency.age()
from cache
Out[8]: 23

In [9]: pency.age()
from cache
Out[9]: 23

In [10]: pency.birthdate = datetime(1998, 9, 10)

In [11]: pency.age()
Out[11]: 24

In [12]: pency.age()
from cache
Out[12]: 24
"""


""" Task 2
Explain the differences between the attributes name, surname and profession, 
and what values they can have in different instances of this class:

class Smith:
    surname = "Smith"
    profession = "smith"

    def __init__(self, name, profession=None):
        self.name = name
        if profession is not None:
            self.profession = profession
"""


""" Task 3
Out of your existing snake game create private repo on your github, create new branch "improve_snake", in that branch
do following steps, try to split work into logical commits like "Create basic classes SnakeGame and Snake",
"Create snake logic", "Add grid colouring", "Fix snake logic", "Refactor code". After finishing work,
merge branch to master.
Snake game using classes.
1. Create class SnakeGame:
    *. attributes:
        1. n_snakes int - how many snakes will play
        2. snakes list['Snake'] - list of alive snakes
        3. fruit Cord - coordinate of fruit
        4. map list[list[str]] - map to display
    *. class attributes:
        1. WIDTH int - define width of the map
        2. HEIGHT int - define height of the map
    *. methods:
        1. create_snake(self, length: int = 3) -> 'Snake' - creates random Snake instance with body length of given
                                                            argument that will fit on the map
        2. update_map(self) -> None - updates self.map attribute with most recent information about snakes and fruit
        3. print_map(self) -> None - prints self.map in nice way
        4. step(self) -> None - handles logic about snakes (calls their methods to turn and move) and fruit, that is,
                                1. for each alive snake:
                                    a) ask snake to update its direction (or not)
                                    b) checks if any snake died and if so deletes it
                                    c) if snake didn't collide move one step while checking if fruit was eaten (if so
                                       spawn new fruit)
                                4. after updating all entities calls self.update_map() and self.print_map()
2. Create class Snake:
    *. attributes:
        1. body: list[Cord] - list of snake body coordinates (tail at self.body[0], head at self.body[-1])
        2. direction: str - one of Snake.DIRECTIONS
        3. game: 'SnakeGame' - SnakeGame object based on which snake will choose it's decisions
    *. class attributes:
        1. DIRECTIONS: tuple[str] - tuple of available directions
        2. DIR_TO_DELTA: dict[str, tuple[int, int]] - how the head should move depending on its head position
    *. methods:
        1. set_direction(self) -> None - given game instance, depending on position of fruit,
                                         it's and other snakes body parts change (or don't) its dir.
        2. move(self, grow: bool = False) -> None - updates its body attribute based on whether it ate the fruit
 
3. Running the game should be as simple as:
if __name__ == '__main__':
    snake_game = SnakeGame(4)
    while True:
        snake_game.step()
        sleep(0.03)
"""


""" Task 4
Create a class called Numbers, which has a single class attribute called MULTIPLIER, and a constructor which
takes the parameters x and y (these should all be numbers).

Write a method called add which returns the sum of the attributes x and y.
Write a class method called multiply, which takes a single number parameter a
and returns the product of a and MULTIPLIER.
Write a static method called subtract, which takes two number parameters, b and c, and returns b - c.
Write a method called value which returns a tuple containing the values of x and y. Make this method into a property,
and write a setter and a deleter for manipulating the values of x and y.
"""


""" Task 5
Create an instance of the Person class from example 2. Use the dir function on the instance. 
Then use the dir function on the class.

1. What happens if you call the __str__ method on the instance? 
   Verify that you get the same result if you call the str function with the instance as a parameter.
2. What is the type of the instance?
3. What is the type of the class?
4. Write a function which prints out the names and values of all the custom attributes of any object that is 
   passed in as a parameter.
"""


""" Task 6
Write a class for creating completely generic objects: its __init__ function should accept any number of keyword 
parameters, and set them on the object as attributes with the keys as names. Write a __str__ method for the 
class – the string it returns should include the name of the class and the values of all the 
object’s custom instance attributes.
"""
