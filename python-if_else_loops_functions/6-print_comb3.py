#!/usr/bin/python3
for first in range(10):
    for second_number in range(first, 10):
        if first != second_number:
            if first != 8 or second_number != 9:
                print("{}{}, ".format(first, second_number), end='')
            elif first == 8 and second_number == 9:
                print("{}{}".format(first, second_number))
