#!/usr/bin/python3

if __name__== "__main__":
    from calculator_1 import add, sub, multiply, divide
    """Print the sum, difference, multiple and quotient of 10 and 5."""

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, multiply(a, b)))
    print("{} / {} = {}".format(a, b, divide(a, b)))
