#!/usr/bin/python3
def roman_to_int(roman_string):
    eldict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
              'D': 500, 'M': 1000}
    num = 0
    letter = 0
    if roman_string:
        for i in roman_string:
            if i in eldict:
                num += eldict[i]
                if letter < eldict[i]:
                    num -= 2 * letter
                    letter = eldict[i]
        return (num)
    return (None)
