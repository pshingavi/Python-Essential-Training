#!python3
__author__ = 'Preetam'

'''This is a demo for while loop
This prints the fibonacci series'''

a, b = 0, 1
while b < 50:
    a, b = b, a+b
    print(b)
print("Done !")

