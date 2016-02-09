#!python3
__author__ = 'Preetam'

import re


def main():
    s = "This is a test for regular expression ! How regular....ascular"

    # Search
    match = re.search('(reg|asc)ular', s)
    if(match):
        print(match.group())    # prints matched word "regular"

        # Substitute
        print(re.sub('(reg|asc)ular', '###', s))

    # PRE COMPILE PATTERN TO AVOID compiling regex each time
    pattern = re.compile('(reg|asc)ular', re.IGNORECASE)

    s = "This is a test for Regular expression ! How Regular....ascular"
    match = re.search(pattern, s)
    print(match.group())

    # Also use it to substitute
    print(pattern.sub('$$$', s))

if __name__ == '__main__':
    main()
