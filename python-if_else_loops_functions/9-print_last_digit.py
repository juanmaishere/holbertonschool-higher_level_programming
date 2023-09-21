#!/usr/bin/python3
def print_last_digit(number):

    if (number >= 0):
        res = number % 10
        print(res, end="")
        return(res)
    else:
        res = number % -10
        res = res * -1
        print(res, end="")
        return(res)
