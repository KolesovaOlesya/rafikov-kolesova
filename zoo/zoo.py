from abc import ABC, abstractmethod

import re


class Zoo(object):
    zoos = []
    animals = []

    def __init__(self, name):
        self.name = name
        Zoo.zoos.append(self)

    @property
    def all_zoo_animals(self):
        zoo_animals = [animal for animal in self.animals if animal.zoo.name == self.name]
        return zoo_animals

    def add_animal(self, animal):
        if isinstance(animal, Feline) or isinstance(animal, Canine):
            Zoo.animals.append(animal)


class Animal:
    __metaclass__ = ABC

    @abstractmethod
    def sound(self):
        pass


class FelineAgeDescriptor(object):
    def __init__(self):
        self.age = None

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Age must be a number!")
        if value <= 0:
            raise ValueError("Age must be greater than 0!")
        self.age = value

    def __get__(self, instance, owner):
        return self.age


class NameDescriptor(object):
    def __init__(self):
        self.name = None

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("The name must be a string!")
        if not re.search('[a-zA-Z]', value):
            raise TypeError("The name must be a letter!")
        self.name = value

    def __get__(self, instance, owner):
        return str(instance.get_kind() + " " + self.name + " from zoo " + instance.zoo.name)


class HabitatDescriptor(object):
    def __init__(self):
        self.habitat = None

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Habitat must be a string!")
        self.habitat = value

    def __get__(self, instance, owner):
        return self.habitat


class LengthDescriptor(object):
    def __init__(self):
        self.length = None

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Length of tail must be a number!")
        self.length = value

    def __get__(self, instance, owner):
        return self.length


class Feline(object):
    def __init__(self, zoo):
        self.zoo = zoo
        self.family = "Feline"
        Zoo.add_animal(zoo, animal=self)

    age = FelineAgeDescriptor()
    name = NameDescriptor()
    habitat = HabitatDescriptor()
    length_of_mustache = LengthDescriptor()

    def info(self):
        print("\nFamily: " + self.family + '\n'
              "name: " + object.__getattribute__(self, "name") + '\n'
              "age: " + str(self.age) + '\n'
              "zoo: " + self.zoo.name + '\n'
              "habitat: " + self.habitat + '\n'
              "length_of_mustache: " + str(self.length_of_mustache) + '\n')

    @classmethod
    def get_kind(cls):
        return cls.kind

    def sound(self):
        pass


class Canine(object):
    def __init__(self, zoo):
        self._age = None
        self.zoo = zoo
        self.family = "Canine"
        Zoo.add_animal(zoo, animal=self)

    name = NameDescriptor()
    habitat = HabitatDescriptor()
    length_of_tail = LengthDescriptor()

    @classmethod
    def get_kind(cls):
        return cls.kind

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be a number!")
        if value <= 0:
            raise ValueError("Age must be greater than 0!")
        self._age = value

    @age.getter
    def age(self):
        return self._age

    def info(self):
        print("\nFamily: " + self.family + '\n'
              "name: " + object.__getattribute__(self, "name") + '\n'
              "age: " + str(self._age) + '\n'
              "zoo: " + self.zoo.name + '\n'
              "habitat: " + self.habitat + '\n'
              "length_of_tail: " + str(self.length_of_tail) + '\n')

    def sound(self):
        pass


class Tiger(Feline):
    kind = "tiger"

    def sound(self):
        print(self.name + " say: growl")


class Cat(Feline):
    kind = "cat"

    def sound(self):
        print(self.name + " say: meow")


class Lion(Feline):
    kind = "lion"

    def sound(self):
        print(self.name + " say: roar")


class Fox(Canine):
    kind = "fox"

    def sound(self):
        print(self.name + " say: snorting")


class Wolf(Canine):
    kind = "wolf"

    def sound(self):
        print(self.name + " say: howl")


def stuff_constructor(self, name, age, zoo):
    self.name = name
    self.age = age
    self.zoo = zoo


def stuff_zoo(self):
    print('I work at the zoo ' + self.zoo.name)


def __setattr__(self, key, value):
    if key == 'name':
        if not isinstance(value, str):
            raise TypeError("The name must be a string!")
        if not re.search('[a-zA-Z]', value):
            raise TypeError("The name must be a letter!")
    elif key == 'age':
        if not isinstance(value, int):
            raise TypeError("Age must be a number!")
        if value <= 0:
            raise ValueError("Age must be greater than 0!")
    elif key == 'zoo':
        if not isinstance(value, Zoo):
            raise TypeError("Invalid entered zoo!")
    object.__setattr__(self, key, value)


Stuff = type('Stuff', (object,), {'__init__': stuff_constructor,
                                  'zoo_name': stuff_zoo,
                                  '__setattr__': __setattr__})

zoo1 = Zoo("Aquarium")
zoo2 = Zoo("Sequoia")

stuff1 = Stuff('Alex', 30, zoo1)
print(stuff1.name)
stuff1.zoo_name()

tiger = Tiger(zoo1)
fox = Fox(zoo1)
wolf = Wolf(zoo1)

tiger2 = Tiger(zoo2)

tiger.age = 10
tiger.name = "Hellman"
tiger.habitat = "India"
tiger.length_of_mustache = 14
print(tiger.age)
print(tiger.name)
print(tiger.habitat)
print(tiger.length_of_mustache)
fox.age = 5
fox.name = "Evanski"
fox.habitat = "North Africa"
fox.length_of_tail = 30
wolf.age = 6
wolf.name = "Kurtis"
wolf.habitat = "Spain"
wolf.length_of_tail = 29
tiger2.age = 20
tiger2.name = "Demetrius"
tiger2.habitat = "China"
tiger2.length_of_mustache = 16

wolf.info()

zoos = Zoo.zoos
print("\nAll zoos: ")
for zoo in zoos:
    print(zoo.name)

zoo1_animals = zoo1.all_zoo_animals

print("\n" + zoo1.name + " animals: ")
for zoo1_animal in zoo1_animals:
    print(zoo1_animal.name)
print("\n")
print(fox.name)
print(tiger.name)

tiger.info()
fox.info()
