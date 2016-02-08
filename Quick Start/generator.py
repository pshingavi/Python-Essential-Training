#!python3
__author__ = 'Preetam'

'''This is a demo to use generator function
A generator is used to create iterator'''


def is_prime(n):
    if n == 1:
        print("1 is special case")
        return False
    for x in range(2,n):
        if n % x == 0:
            #print("{} is not prime".format(n))
            return False
    else:
        #print("{} is prime".format(n))
        return True


def primes_generator(num = 1):
    while True:
        if is_prime(num) : yield num
        num += 1

for num in primes_generator():
    if num > 100:
        break
    print(num)