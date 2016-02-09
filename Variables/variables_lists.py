#!python3
__author__ = 'Preetam'


# Python has several sequential things or lists
# Use tuple when fixed list , it's faster than mutable list
def main():
    #########
    # TUPLE
    #########

    # Tuple is a immutable object, cannot insert / delete / operate to update
    x = (1, 2, 3)
    print(type(x), x)   #<class 'tuple'> (1, 2, 3)

    # Can't do add / delete / update
    print(x[1])
    # x[1] = 3 Tuple object doesn't support item assignment

    ########
    # LISTS
    ########
    x = [1, 2, 3]
    print(type(x), x)   #<class 'list'> [1, 2, 3]

    x.append(4)
    print(x)
    x.insert(2,10)
    print(x)

    for item in x:
        print(item)

    s = "welcome"
    for item in s:
        print(item)


if __name__ == '__main__':
    main()