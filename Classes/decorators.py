#!python3
__author__ = 'Preetam'

# Decorators are functions that return other functions and are used to modify other function's working
# Decorators help create accessor methods for variables


class Duck:
    def __init__(self, **kwargs):
        self.properties = kwargs

    def get_property(self, property_name):
        return self.properties.get(property_name, None)

    def set_property(self, property_name, property_value):
        self.properties[property_name] = property_value

    # Let's define a variable color as an accessor
    @property   # This defines color as an accessor and also as a getter method
    def color(self):
        return self.properties.get('color', None)

    # Create setter and deleter method for the above property
    @color.setter
    def color(self, c):
        self.properties['color'] = c

    @color.deleter
    def color(self):
        print("Deleting...")
        del self.properties['color']


def main():
    donald = Duck(color='white')
    print(donald.get_property('color'))

    # Use decorators
    donald.color = 'blue'   # Calls setter
    print("Now color is", donald.color)  # Calls getter

    del donald.color    # Calls deleter
    print("After delete color is", donald.color)  # None
    # Above does not create any side effects, the setter / getter / deleter method definitions are handled in the class


if __name__ == '__main__':
    main()