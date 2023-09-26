#!/usr/bin/python3
def uniq_add(my_list=[]):
    exclude = []
    num = 0
    for i in my_list:
        if i not in exclude:
            num += i
            exclude.append(i)
    return(num)
