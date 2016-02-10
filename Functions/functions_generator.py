#!python3
__author__ = 'Preetam'


def main():
    # Non inclusive range default, print 0 - 24 below
    for n in range(0,25):   # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
        print(n, end=' ')

    print('\nInclusive')
    # To create inclusive range function, write a generator
    start = 0
    stop = 25
    step = 1
    for n in inclusive_range(start,stop, step): # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
        print(n, end=' ')

    print('\nInclusive revised with 1 arg')
    for n in revised_inclusive_range(25):   # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
        print(n, end=' ')

    print('\nInclusive revised with 2 arg')
    for n in revised_inclusive_range(25, 35):   # 25 26 27 28 29 30 31 32 33 34 35
        print(n, end=' ')

    print('\nInclusive revised with 3 arg')
    for n in revised_inclusive_range(25, 35, 5):    # 25 30 35
        print(n, end=' ')

    # Try raising exception condition from revised method
    try:
        print('\nInclusive revised with >3 args')
        for n in revised_inclusive_range(25, 35, 5, 1, 3):    # Exception : At most 3 arguments required, got 5
            print(n, end=' ')
    except TypeError as e:
        print("Exception : {}".format(e))


# Generator function to generate inclusive range values
def inclusive_range(start, stop, step):
    num = start
    while num <= stop:
        yield num
        num += step


# Revised method imitating the actual range function
def revised_inclusive_range(*args):
    num_args = len(args)
    if num_args < 1:
        raise ValueError("Requires at least one argument")
    elif num_args == 1:
        start = 0
        stop = args[0]
        step = 1
    elif num_args == 2:
        (start,stop) = args
        step = 1
    elif num_args == 3:
        (start, stop, step) = args
    else:
        raise TypeError("At most 3 arguments required, got {}".format(len(args)))
    num = start
    while num <= stop:
        yield num
        num += step


if __name__ == '__main__':
    main()