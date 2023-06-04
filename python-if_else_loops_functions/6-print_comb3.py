#!/usr/bin/python3
for tens_d in range(0, 10):
    for ones_d in range(tens_d + 1, 10):
        print("{:d}{:d}".format(tens_d % 10, ones_d % 10), end=', ')
print('')
