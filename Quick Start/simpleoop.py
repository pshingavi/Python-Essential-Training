#!python3
__author__ = 'Preetam'

'''This is a demo for Reusing data and code using class'''


class Fibonacci:
    # Define a constructor
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Define a generator function to generate a sequence of fibonacci series
    def series(self):
        while True:
            yield self.b
            self.a, self.b = self.b, (self.a + self.b)

# Instantiate the class object
f = Fibonacci(0,1)
for n in f.series():
    if n > 100:
        break
    print(n)