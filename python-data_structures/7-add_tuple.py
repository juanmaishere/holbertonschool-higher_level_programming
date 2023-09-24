#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    num2 = 0
    num1 = 0
    if len(tuple_b) >= 1:
        num1 += tuple_b[0]
    if len(tuple_b) >= 2:
        num2 += tuple_b[1]

    if len(tuple_a) >= 1:
        num1 += tuple_a[0]
    if len(tuple_a) >= 2:
        num2 += tuple_a[1]

    tuple = (num1, num2)
    return tuple
