#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        1d = number % 10
    else:
        1d = number % -10
        1d *= -1
    print("{:d}".format(1d), end='')
    return (1d)
