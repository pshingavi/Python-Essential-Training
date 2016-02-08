#!python3
__author__ = 'Preetam'

try:
    fh = open("abc.txt")
    for line in fh.readlines():
        print(line)
except IOError as e:
    print("Something wrong happened ({})".format(e))

print("After exception !!!")