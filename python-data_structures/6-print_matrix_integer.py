#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    if matrix:
        for row in matrix:
            for i, element in enumerate(row):
                # Format each element
                print("{:d}".format(element), end="")
                # Add space if it's not the last element in the row
                if i < len(row) - 1:
                    print(" ", end="")
            print()
