#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lens = len(my_list) - 1

    while lens >= 0:
        print("{:d}".format(my_list[lens]))
        lens = lens - 1
