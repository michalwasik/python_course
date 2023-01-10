# 20:55
# employees = [
#     ["James Kirk", 34, "Captain", 2265],
#     ["Spock", 35, "Science Officer", 2254],
#     ["Leonard McCoy", "Chief Medical Officer", 2266],
# ]


class Dog:
    breed = 'Doberman'

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        # self.breed = 'new breed'

    def is_old(self) -> bool:
        return self.age > 10

    def speak(self, sound: str) -> str:
        return f"{self.name} barks {sound}"

    def is_scared_of_malamut(self, malamut_dog: 'MalamutDog'):
        return malamut_dog.kill_count > 10

    def __str__(self):
        return f'Dog instance {self.name}'


# print(Dog.breed)
# print(f'{Dog = }')
dog_1 = Dog('Coco', age=7)
dog_2 = Dog('Zabek', age=13)
dog_3 = Dog('Figa', age=1)
# print(f'{dog_1 = }')
# print(f'{dog_1.breed = }')
# Dog.breed = 'Class Attr'
# print(f'{dog_1.breed = }')
# dog_1.test = 'abc'
# dog_1.breed = 'Instance Attr'
# print(f'{dog_1.breed = }')
# print(f'{Dog.breed = }')
# print(dog_1.name)

# print(Dog.a)
# print(Dog().add(1, 2))

# print(isinstance(dog_1, Dog))
# print(isinstance(dog_2, Dog))
# print(dog_1, dog_2)
# print(dog_1 == dog_2)
# print(type(dog_1) == type(dog_2))

# print(f'{dog_1.is_old() = }')
# print(f'{dog_2.is_old() = }')
# print(f'{dog_3.is_old() = }')

# print(dog_2.speak('haha'))
# print(dog_2)


class MalamutDog(Dog):
    breed = 'Malamut'
    kill_count = 0

    def is_old(self) -> bool:
        return self.age > 12

    def speak(self, sound: str = "I'm the best dog!") -> str:
        # return f"{self.name} says {sound}"
        # return Dog.speak(self, sound)
        return super().speak(sound)


dino = MalamutDog(name='Dino', age=9)
dino.kill_count = 13
print(f'{dino.is_old() = }')
print(dino.speak())


def add_dogs(dog_a: 'Dog', dog_b: 'Dog') -> int:
    return dog_a.age + dog_b.age
