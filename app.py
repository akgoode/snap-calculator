from calculator import Calculator


def multiply(val1, val2):
    return val1 * val2


def add(val1, val2):
    return val1 + val2


def subtract(val1, val2):
    return val1 - val2


def divide(val1, val2):
    return val1 / val2


def power(val1, val2):
    return val1**val2


operations = {"*": multiply, "+": add, "-": subtract, "/": divide, "^": power}


c = Calculator(operations)

while True:
    user_input = input("> ")
    if user_input == "q":
        break
    else:
        result = c.input(user_input)
        print(result)
