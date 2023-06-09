#!/usr/bin/python3
def multiple_returns(sentence):
    x = len(sentence)
    if len(sentence) > 0:
        tuple = x, sentence[0]
    else:
        tuple = (x, None)
    return tuple
