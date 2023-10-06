#!/usr/bin/python3
""" Summary """


class MyList(list):
    """
    My list class with
    print_sorted print all list
    """
    def print_sorted(self):
        """
        print the list
        in order alphabetical
        """
        if all(isinstance(x, int) for x in self):
            print(sorted(self))
