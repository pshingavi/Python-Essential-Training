#!python3
__author__ = 'Preetam'


def main():
    try:
        filename = 'lines.doc'
        for line in read_file(filename):
            print(line, end="")
    except IOError as e:
        print("Something is wrong {}".format(e))
    except ValueError as e: # Catch the custom exception
        print('Value error : {}'.format(e))


def read_file(filename):
    if(filename.endswith('.txt')):
        fh = open(filename)
        return fh.readlines()
    else:
        raise ValueError('Filename must end with .txt')

if __name__ == '__main__':
    main()