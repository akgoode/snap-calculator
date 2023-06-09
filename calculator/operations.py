def multiply(val1, val2):
    return val1 * val2


def add(val1, val2):
    return val1 + val2


def subtract(val1, val2):
    return val1 - val2


def divide(val1, val2):
    return round(val1 / val2, 3)


operations = {"*": multiply, "+": add, "-": subtract, "/": divide}
