#!python3
__author__ = 'Preetam'


# main function
def main():
    duck = Duck()
    print(duck.get_variable('color'))   # None

    new_duck = Duck(color='white')
    print(new_duck.get_variable('color'))   # white

    another_new_duck = Duck(color='yellow', description='This is another new duck')
    print(another_new_duck.get_variable('description'))  # This is another new duck


# Class Duck
class Duck:

    # Constructor, set _variables dictionary
    def __init__(self, **kwargs):
        self._variables = kwargs

    # Get a variable from dictionary
    def get_variable(self, k):
        return self._variables.get(k, None)

    # Set a key in the variables dict
    def set_variable(self, k, v):
        self._variables[k] = v


if __name__ == '__main__':
    main()