#!python3
__author__ = 'Preetam'

'''This is a demo for for loop
This prints the lines of a file'''

fh = open("lines.txt")

for line in fh.readlines():
    print(line, end="")

print("\nDone reading the file !")