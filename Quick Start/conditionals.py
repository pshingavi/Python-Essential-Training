#!python3
__author__ = 'Preetam'

'''This is demo to use python3 conditionals'''

a, b = 0, 1

if(a > b):
    print("a : ({}) is greater than b : ({})".format(a,b))
else:
    print("b : ({}) is greater than a : ({})".format(b,a))

#print((a<b) ? a : b)
print("a greater" if a > b else "b greater")