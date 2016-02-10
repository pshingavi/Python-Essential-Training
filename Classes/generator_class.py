#!python3
__author__ = 'Preetam'


def main():
    try:
        for o in inclusive_range(10,20,1):
            print(o, end=' ')   # 10 11 12 13 14 15 16 17 18 19 20
    except TypeError as e:
        print("Exception : {}", e)


# inclusive_range as class
class inclusive_range:

    # Init method to set start, stop, step values
    def __init__(self, *args):
        arg_length = len(args)
        if arg_length == 0:
            raise TypeError("Expecting at least one argument")
        elif arg_length == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif arg_length == 2:
            (self.start, self.stop) = args
            self.step = 1
        elif arg_length == 3:
            (self.start, self.stop, self.step) = args
        else:
            raise TypeError("Expecting at most 3 args, got {}".format(len(args)))

    # Overwrite a __iter__ method to make the object iteratible
    def __iter__(self):
        i = self.start
        while i <= self.stop:
            yield i
            i += self.step

if __name__ == '__main__':
    main()