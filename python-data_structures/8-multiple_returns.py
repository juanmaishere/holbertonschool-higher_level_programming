#!/usr/bin/python3
def multiple_returns(sentence):
    
    if (sentence):
        lens = len(sentence)
        a = sentence[0]
        tuple = (lens, a)
        return (tuple)
    
    tuple = (lens, None)
    return(tuple)
