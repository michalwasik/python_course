# Task 1
import datetime


class Person:
    def __init__(self, birthdate: datetime.datetime):
        self.birthdate = birthdate
        self._age: int | None = None
        self._last_bd = birthdate

    # def __setattr__(self, name, value):
    #     if name == 'birthdate':
    #         self._age = None
    #     super().__setattr__(name, value)     # ochuj

    def age(self):
        if self._age and self.birthdate == self._last_bd:
            print('from cache')
            return self._age
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        self._age = age
        self._last_bd = self.birthdate
        return self._age

#
# pency = Person(datetime.datetime(1999, 4, 15))
# print(pency.age())
# print(pency.age())
# print(pency.age())
# pency.birthdate = datetime.datetime(1998, 9, 10)
# print(pency.age())
# print(pency.age())
#

# Task 2

'''
surname is a class attribute, if not changed all instances would have the same surname value.
name is a instance attribute, defined while creating instance.
profession is both class and instance attribute. If not defined within instance, it behaves as a class attribute, 
otherwise it is instance attribute. 
'''

# Task 3

# jprdl : #

# Task 4


class Numbers:
    MULTIPLIER = 2

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def sum(self):
        return self.x + self.y

    @classmethod
    def multiply(cls, a: int):
        return a * cls.MULTIPLIER

    @staticmethod
    def subtract(b: int, c: int):
        return b - c

    @property
    def value(self):
        return self.x, self.y

    @value.setter
    def value(self, values: tuple):
        self.x, self.y = values

    @value.deleter
    def value(self):
        del self.x
        del self.y


# fourfive = Numbers(4, 5)
# print(fourfive.multiply(4))
# print(fourfive.subtract(99, 3))
# print(fourfive.value)
# fourfive.value = (6, 2)
# print(fourfive.value)
# del fourfive.value
# print(fourfive.value)

# Task 5
class Smith:
    surname = "Smith"
    profession = "smith"

    def __init__(self, name, profession=None):
        self.name = name
        if profession is not None:
            self.profession = profession


janek = Smith('Janek', 'welder')
# print(dir(janek))   # class methods + instance attributes
# print(dir(Smith))   # class methods + class attributes
# print(janek.__str__())
# print(str(janek))
# print(type(janek))  # object of Smith class
# print(type(Smith))  # type


def custom_attr(obj):
    return list(obj.__dict__.keys())


# print(custom_attr(janek))

# Task 6

class GenericClass:
    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)

    def __str__(self):
        return f'''Class name: GenericClass
custom instance attributes:
{list(self.__dict__.items())}'''


obj1 = GenericClass(a=1, b=2, c=3)
# print(obj1.__str__())
