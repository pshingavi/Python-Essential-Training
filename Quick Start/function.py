#!python3
__author__ = 'Preetam'

'''This is a demo for a reusable function
Write a function to print prime numbers'''


def is_prime(n):
    if n == 1:
        print("1 is special")
        return False
    for x in range(2,n):
        if (n % x) == 0:
            # not prime
            print("{} is {} x {}".format(n, x, int(n/x)))
            return False
    else:
        # Prime
        print("{} is prime".format(n))
        return True

for n in range(1,30):
    is_prime(n)