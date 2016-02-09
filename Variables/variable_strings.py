#!python3
__author__ = 'Preetam'

# Strings in python are IMMUTABLE objects

# String with \n
s = "This is a \nstring"
print(s)
print(id(s))    #1

s = "This is a string"
print(id(s))    #2
s = "This is a \nstring"
print(id(s))    # prints same id as #1

# Raw string - Ignores \n like characters
s2 = r"This is a \nstring"
print(s2)

# Format method
n = 42
print("The number is {}".format(n))

# Multiple line string
lines = '''\
This is a multiple
line string
'''
print(lines)