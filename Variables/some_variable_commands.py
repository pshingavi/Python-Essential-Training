#!python3
__author__ = 'Preetam'

# IMMUTABLE Stuff
x = 42
print(id(x), id(x)) # Same since immutable
y = 42
print(x == y)   # True, compares value
print(x is y)   # True, compares Id

# MUTABLE stuff
x = dict(x=1)
y = dict(x=1)
print(id(x), id(y)) # Print different id sicne mutable objects
print(x == y)   # True, content is same
print(x is y)   # False, Id is different

# Specifying logical values with True and False
a, b = 0, 1
print(a == b)   # False
# Boolean - immutable like strings / tuple
print(id(True))
print(id(1==1)) # Same as above