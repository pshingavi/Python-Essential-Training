#!python3
__author__ = 'Preetam'


'''This is a demo to show inheritance and data abstraction in python'''


# Class definition for AnimalActions
class AnimalActions:
    def quack(self):
        return self.strings["quack"]

    def feathers(self):
        return self.strings["feathers"]

    def bark(self):
        return self.strings["bark"]

    def fur(self):
        return self.strings["fur"]


# Class Duck with parent class as AnimalActions
class Duck(AnimalActions):
    strings = dict(
        quack="Duck quacks",
        feathers="Duck has grey and white feathers",
        bark="Duck doesn't bark !",
        fur="Duck has no fur"
    )


# Class Person with parent class as AnimalActions
class Person(AnimalActions):
    strings = dict(
        quack="Person doesn't quack",
        feathers="Person has grey and white feathers",
        bark="Person says woooof !",
        fur="Person has no fur"
    )


# Class Dog with parent class as AnimalActions
class Dog(AnimalActions):
    strings = dict(
        quack="Dog doesn't quack",
        feathers="Dog has grey and white feathers",
        bark="Dog Barks",
        fur="Dog has no fur"
    )


# In the lake method for duck
def in_the_lake(duck):
    print(duck.quack())
    print(duck.feathers())


# In the dog house for dog
def in_the_doghouse(dog):
    print(dog.bark())
    print(dog.feathers())


# Main function body
def main():
    donald = Duck()
    john = Person()
    rocky = Dog()

    # Print the lake and dogouse methods for each
    print("In the lake...")
    for animal in (donald, john, rocky):
        in_the_lake(animal)

    print("In the doghouse...")
    for animal in (donald, john, rocky):
        in_the_doghouse(animal)


# If module main call main()
if __name__ == '__main__':
    main()