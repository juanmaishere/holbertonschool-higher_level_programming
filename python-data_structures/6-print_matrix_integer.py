#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    if matrix:
        for row in matrix:
            for element in row:
                if element == len(row):
                    print("{:d}".format(element), end="")
                else:
                    print("{:d}".format(element), end=" ")
            print()
