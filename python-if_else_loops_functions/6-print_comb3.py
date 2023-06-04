#!/usr/bin/python3
for tens_digit in range(0, 10):
    for ones_digit in range(tens_digit + 1, 10):
        print(f"{tens_digit}{ones_digit:0}", end=", ")
print()
