#!python3
__author__ = 'Preetam'


# Working with associative arrays - Dictionaries
def main():

    # Naive way of working with dict
    d = {"one": 1, "two": 2, "three": 3}

    print("*********Not Sorted*********")
    for k in d:
        print(k, d[k])

    # print sorted
    print("*********Sorted*********")
    for k in sorted(d.keys()):
        print(k, d[k])

    # Better way to work with dic
    d = dict(
        one=1, two=2, three=3, four='four'
    )
    # Dict objects are mutable - Example insert
    d['six'] = 6

    # print sorted
    print("*********Sorted*********")
    for k in sorted(d.keys()):
        print(k, d[k])

if __name__ == '__main__':
    main()