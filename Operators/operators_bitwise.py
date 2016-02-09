#!python3
__author__ = 'Preetam'


# Print int as binary 8 bits
def binary(num):
    print("{:08b}".format(num))

def main():
    a = 0b0101
    print(a, type(a))  # prints 5 <class 'int'>

    # To print binary format the
    binary(5)

    x, y = 0x55, 0xaa
    print(x)    # 85
    binary(x)   #01010101
    binary(y)
    # Or
    binary(x | y)
    # And
    binary(x & y)
    # Exclusive OR
    binary(x ^ y)   #11111111
    binary(x ^ 0)   #01010101
    binary(x ^ 0xff)    # Flip bits : 10101010

    # Left Shift
    binary(x << 4)
    # Right Shift
    binary(x >> 4)
    # Negation
    binary(~ x) #-10101010

    print([1,2] == [2,1])   # False
    print([1,2] == [1,2])   # True
    print([1,2] is [1,2])   # False
    print(id((1,2)) == id((1,2)))   # False although immutable


if __name__ == '__main__':
    main()