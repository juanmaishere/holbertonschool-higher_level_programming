#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    printed = 0
    while i < x:
        if isinstance(my_list[i], list):
            i += 1
            continue
        
        try:
            number = int(my_list[i])
            print("{:d}".format(number), end="")
            printed += 1
        except ValueError:
            pass
        finally:
            i += 1
    print()

    return printed
