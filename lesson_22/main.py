# keys = ['a', 'b', 'c']
#
# my_dict = {'b': 10, 'c': 100}
# # for key in keys:
# #     print(my_dict.get(key))
#
#
# class Empty:
#     b = 10
#
#
# empty = Empty()
# # for key in keys:
# #     print(getattr(empty, key, None))
# #
# # setattr(empty, 'b', 'Michal')
# # print(f'{empty.b = }')
#
# for key, value in my_dict.items():
#     setattr(empty, key, value)
#
# for key, value in my_dict.items():
#     print(getattr(empty, key))


# class Student:
#     _school_name = 'XYZ School'  # class attribute
#
#     def __init__(self, name, age):
#         self._name: str = name  # instance attribute
#         self._age: str = age  # instance attribute
#
#     def print_my_name(self):
#         print(self._name.capitalize())
#
#
# std = Student('Michal', 13)
# print(std._name)
# std.print_my_name()


# class Student:
#     __school_name = 'XYZ School'  # class attribute
#
#     def __init__(self, name, age):
#         self.__name: str = name  # instance attribute
#         self.__age: str = age  # instance attribute
#
#     def print_my_name(self):
#         print(self.__name.capitalize())
#
#
# std = Student('Michal', 13)
# std._Student__name = 'filip'
# std.print_my_name()


# import datetime
# from functools import cache
#
#
# class Person:
#
#     def __init__(self, birthdate: datetime.datetime):
#         self.birthdate = birthdate
#         self.best_friend = None
#
#     def set_best_friend(self, person: 'Person'):
#         self.best_friend = person
#
#     @cache
#     def age(self):
#         print('calculating age')
#         today = datetime.date.today()
#         age = today.year - self.birthdate.year
#
#         if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
#             age -= 1
#
#         return age
#
#
# person = Person(datetime.datetime(2000, 1, 2))
# print(person.age())
# print(person.age())
# print(person.age())
# person.birthdate = datetime.datetime(2022, 1, 2)
# print(person.age())


class PolishPerson:
    COUNTRY = 'PL'

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def who_am_i(self):
        return f"I'm small Polish person {self.full_name}"

    @classmethod
    def where_am_i_from(cls):
        return f"I'm from {cls.COUNTRY}"

    @classmethod
    def create_anonymous(cls, first_name: str):
        return cls(first_name, "Kowalski")

    @staticmethod
    def best_country():
        return 'Poland'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @full_name.setter
    def full_name(self, value: str):
        first_name, last_name = value.split()
        self.first_name = first_name
        self.last_name = last_name

    def __eq__(self, other):
        return self.first_name == other


# person = PolishPerson('Michal', 'Babula')
# print(person.who_am_i())
# print(PolishPerson.where_am_i_from())
# print(person.full_name)
# new_person = PolishPerson.create_anonymous('Monika')
# print(new_person.full_name)
#
# person.full_name = 'Michał Tęcza'
# print(person.last_name)

person = PolishPerson('Felipe', 'Morales')
for key in dir(person):
    print(f'{key} = {getattr(person, key)}')
print(person == 'Felipe')
# print(PolishPerson.__class__)
# Here are some examples of special object properties:

# __init__: the initialisation method of an object, which is called when the object is created.
# __str__: the string representation method of an object, which is called when you use the str
#          function to convert that object to a string.
# __class__: an attribute which stores the the class (or type) of an object – this is what is
#            returned when you use the type function on the object.
# __eq__: a method which determines whether this object is equal to another.
#         There are also other methods for determining if it’s not equal, less than, etc..
#         These methods are used in object comparisons, for example when we use
#         the equality operator == to check if two objects are equal.
# __add__ is a method which allows this object to be added to another object.
#         There are equivalent methods for all the other arithmetic operators.
#         Not all objects support all arithemtic operations – numbers have all of these methods defined,
#         but other objects may only have a subset.
# __iter__: a method which returns an iterator over the object – we will find it on strings,
#           lists and other iterables. It is executed when we use the iter function on the object.
# __len__: a method which calculates the length of an object – we will find it on sequences.
#          It is executed when we use the len function of an object.
# __dict__: a dictionary which contains all the instance attributes of an object,
#           with their names as keys. It can be useful if we want to iterate over all the
#           attributes of an object. __dict__ does not include any methods,
#           class attributes or special default attributes like __class__.


print(person.__dict__.items())


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __eq__(self, other):  # does self == other?
        return self.name == other.name and self.surname == other.surname

    def __gt__(self, other):  # is self > other?
        if self.surname == other.surname:
            return self.name > other.name
        return self.surname > other.surname

    # now we can define all the other methods in terms of the first two

    def __ne__(self, other):  # does self != other?
        return not self == other  # this calls self.__eq__(other)

    def __le__(self, other):  # is self <= other?
        return not self > other  # this calls self.__gt__(other)

    def __lt__(self, other):  # is self < other?
        return not (self > other or self == other)

    def __ge__(self, other):  # is self >= other?
        return not self < other
