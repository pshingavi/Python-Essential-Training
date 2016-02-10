#!python3
__author__ = 'Preetam'


# Define main function
def main():
    stub_method()   # Call stub method
    arguments_test(1, 2, 3, 5, 6, 7)
    kw_arguments_test(1, 2, 3, one=1, two=2, three=3)

# *args is a list of arguments as tuple
def arguments_test(a=None, b=None, c=None, *args_tuple):
    print(a, b, c, args_tuple)  # 1 2 3 (5, 6, 7)


# **kwargs is a dictionary of arguments OR named arguments
def kw_arguments_test(a=None, *args, **kwargs):
    print("Pure argument : ", a)  # 1
    print("Tuple list arguments *args : ", args)  # (2,3)
    print(kwargs)   # {'two': 2, 'three': 3, 'one': 1}
    print(kwargs['one'])    # 1

# Some stub which is currently as a placeholder
def stub_method():
    pass

if __name__ == '__main__':
    main()