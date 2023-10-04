#!/bin/usr/python3
"""
my list class with method for printing
"""


class MyList(list):
    """
    My list class with
    :print_sorted print all list
    """
    def print_sorted(self):
        self = sorted(self)
        print(self)
