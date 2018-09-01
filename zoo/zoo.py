from abc import ABC, abstractmethod


class Zoo:
    zoos = []
    animals = []

    def __init__(self, name):
        self.name = name
        Zoo.zoos.append(self)

    def add_animal(self):
        Zoo.animals.append(self)


class Animal:
    __metaclass__ = ABC

    def __init__(self, name, age, zoo, habitat):
        self.name = name
        self.age = age
        self.zoo = zoo
        self.habitat = habitat

    def __setattr__(self, name, value):
        if name == 'name':
            if type(value) is not str:
                raise TypeError("The name must be a string!")
        elif name == 'age':
            if type(value) is not int:
                raise TypeError("Age must be a number!")
        elif name == 'zoo':
            if type(value) is not Zoo:
                raise TypeError("Zoo must be a Zoo type!")
        elif name == 'habitat':
            if type(value) is not str:
                raise TypeError("Habitat must be a string!")
        elif name == 'length_of_tail':
            if type(value) is not int:
                raise TypeError("Length of tail must be a number!")
        elif name == 'length_of_mustache':
            if type(value) is not int:
                raise TypeError("Length of mustache must be a number!")
        elif name == 'family':
            if type(value) is not str:
                raise TypeError("Family must be a string!")
        object.__setattr__(self, name, value)

    @abstractmethod
    def sound(self):
        pass


class Feline(Animal, Zoo):
    def __init__(self, name, age, zoo, habitat, length_of_mustache):
        super().__init__(name, age, zoo, habitat)
        self.length_of_mustache = length_of_mustache
        self.family = "Feline"
        Zoo.add_animal(self)

    def info(self):
        print("\nFamily: " + self.family + '\n'
              "name: " + self.name + '\n'
              "age: " + str(self.age) + '\n'
              "zoo: " + self.zoo.name + '\n'
              "habitat: " + self.habitat + '\n'
              "length_of_mustache: " + str(self.length_of_mustache) + '\n')

    def sound(self):
        pass


class Canine(Animal, Zoo):
    def __init__(self, name, age, zoo, habitat, length_of_tail):
        super().__init__(name, age, zoo, habitat)
        self.length_of_tail = length_of_tail
        self.family = "Canine"
        Zoo.add_animal(self)

    def info(self):
        print("\nFamily: " + self.family + '\n'
              "name: " + self.name + '\n'
              "age: " + str(self.age) + '\n'
              "zoo: " + self.zoo.name + '\n'
              "habitat: " + self.habitat + '\n'
              "length_of_tail: " + str(self.length_of_tail) + '\n')

    def sound(self):
        pass


class Tiger(Feline, Zoo):
    kind = "tiger"

    def sound(self):
        print(self.name + " say: growl")


class Cat(Feline, Zoo):
    kind = "cat"

    def sound(self):
        print(self.name + " say: meow")


class Lion(Feline, Zoo):
    kind = "lion"

    def sound(self):
        print(self.name + " say: roar")


class Fox(Canine, Zoo):
    kind = "fox"

    def sound(self):
        print(self.name + " say: snorting")


class Wolf(Canine, Zoo):
    kind = "wolf"

    def sound(self):
        print(self.name + " say: howl")


zoo1 = Zoo("Aquarium")
zoo2 = Zoo("Sequoia")

tiger = Tiger("Hellman", 10, zoo1, "India", 14)
cat = Cat("Jenniffer", 4, zoo1, "Russia", 5)
lion = Lion("Leo", 9, zoo1, "East Africa", 12)
fox = Fox("Evanski", 2, zoo1, "North Africa", 30)
wolf = Wolf("Kurtis", 6, zoo1, "Spain", 29)

tiger2 = Tiger("Demetrius", 20, zoo2, "China", 16)
cat2 = Cat("Bagira", 8, zoo2, "South America", 7)
lion2 = Lion("Sammie", 12, zoo2, "India", 13)
fox2 = Fox("Ismael", 5, zoo2, "South China", 56)
wolf2 = Wolf("Will", 8, zoo2, "Russia", 50)

wolf.info()
wolf2.info()
lion2.sound()
cat.sound()

zoos = Zoo.zoos
print("\nAll zoos: ")
for zoo in zoos:
    print(zoo.name)

animals = Zoo.animals
zoo1_animals = [animal for animal in animals if animal.zoo.name == zoo1.name]

print("\n" + zoo1.name + " animals: ")
for zoo1_animal in zoo1_animals:
    print(zoo1_animal.name)
