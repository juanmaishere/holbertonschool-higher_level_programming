#!/usr/bin/python3
def add(a, b):
    if (a < 0):
        res = b - (-a)
    elif (b < 0):
        res = a - (-b)
    else:
        res = a + b
    return(res)
