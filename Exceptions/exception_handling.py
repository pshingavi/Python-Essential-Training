#!python3
__author__ = 'Preetam'


def main():
    try:
        fh = open('random_file.txt')
        for line in fh.readlines():
            print(line, end="")
    except IOError as e:
        print("Something is wrong {}".format(e))


if __name__ == '__main__':
    main()