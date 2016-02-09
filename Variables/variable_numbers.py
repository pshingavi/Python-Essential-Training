#!python3
__author__ = 'Preetam'

x = 42
print(type(x), x)
#<class 'int'> 42

x = 42.0
print(type(x), x)
#<class 'float'> 42.0

x = 42 / 9
print(type(x), x)
#<class 'float'> 42.0

# Integer division
x = 42 // 9
print(type(x), x)
#<class 'int'> 42

# Round division value returned
x = round(42 / 9)
print(type(x), x)
#<class 'int'> 5

# Round division value with decimals returned
x = round(42 / 9, 2)
print(type(x), x)
#<class 'float'> 4.67

# USE int constructor
x = int(42/9)
print(type(x), x)
#<class 'int'> 4

# USE float constructor
x = float(42)
print(type(x), x)
#<class 'float'> 42.0