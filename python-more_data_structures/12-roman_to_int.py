#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    romSum = 0
    converter = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    for current, next in zip(roman_string, roman_string[1:]):
        if converter[current] >= converter[next]:
            romSum += converter[current]
        else:
            romSum -= converter[current]
    romSum += converter[roman_string[-1]]
    return romSum
