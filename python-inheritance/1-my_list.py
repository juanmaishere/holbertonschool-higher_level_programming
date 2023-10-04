#!/usr/bin/python3
"""
my list class with method for printing
you can assume its a list
"""


class MyList(list):
    """
    My list class with
    :print_sorted print all list
    """
    def print_sorted(self):
        """
        print the list
        """
        print(sorted(self))