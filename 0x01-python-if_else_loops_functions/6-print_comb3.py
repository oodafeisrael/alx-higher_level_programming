#!/usr/bin/python3
for tens_dgt in range(9):
    for unit_dgt in range(tens_dgt + 1, 10):
        if tens_dgt * 10 + unit_dgt < 89:
            print("{:d}{:d}".format(tens_dgt, unit_dgt), end=", ")
print("{:d}".format(89))
