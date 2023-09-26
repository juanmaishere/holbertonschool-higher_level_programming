#!/usr/bin/python3
def best_score(a_dictionary):
    best = 0
    key = None
    if a_dictionary:
        for i, value in a_dictionary.items():
            if value > best:
                best = value
                key = i
        return (key)
    return (None)
