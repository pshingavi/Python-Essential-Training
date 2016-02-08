#!python3
__author__ = 'Preetam'

'''This is a demo to show MVC pattern in python'''


# -- VIEW -- Seen from the AnimalActions class
class AnimalActions:
    # Quack
    def quack(self):
        return self._do_action("quack")

    # Bark
    def bark(self):
        return self._do_action("bark")

    # Feather
    def feather(self):
        return self._do_action("feather")

    # Fur
    def fur(self):
        return self._do_action("fur")

    # Underscore says this method is just used inside this class
    def _do_action(self, action):
        if action in self.strings:
            return self.strings[action]
        else:
            return "The {} has no {}".format(self.animal_name(),action)

    # Show animal name from name of the class
    def animal_name(self):
        return self.__class__.__name__.lower()


# Class Duck
class Duck(AnimalActions):
    strings = dict(
        quack = "Duck quacks",
        feather = "Duck has grey and white feathers",
        fur = "Duck has fur"
    )


# Class Person
class Person(AnimalActions):
    strings = dict(
        bark = "Person says woooof !"
    )


# Class Dog
class Dog(AnimalActions):
    strings = dict(
        bark = "Dog barks"
    )


# In the lake method for duck
def in_the_lake(duck):
    print(duck.quack())
    print(duck.feather())
    print(duck.fur())


# In the dog house for dog
def in_the_doghouse(dog):
    print(dog.bark())
    print(dog.feather())


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
