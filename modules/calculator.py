# calculator.py
def add(a, b):

    # return the sum of  a and b
    return a + b


def subtract(a, b):
    # return the difference of a nad b
    return a - b


def multiply(a, b):
    # return the she multiplication of a and b
    return a * b


def divide(a, b):
    # return the division of a by b
    if b == 0:
        return "Error! Division by zero."
    return a / b
