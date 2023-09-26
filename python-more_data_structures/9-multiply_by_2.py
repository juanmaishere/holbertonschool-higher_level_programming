#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for key, j in a_dictionary.items():
        new_dict[key] = j * 2
    return(new_dict)
