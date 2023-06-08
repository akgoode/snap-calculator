def multiply(val1, val2):
    return val1 * val2


def add(val1, val2):
    return val1 + val2


def subtract(val1, val2):
    return val1 - val2


def divide(val1, val2):
    return val1 / val2


operations = {"*": multiply, "+": add, "-": subtract, "/": divide}


def calculate(items):
    stack = []
    for item in items:
        if item not in operations.keys():
            stack.append(item)
        else:
            second = int(stack.pop())
            first = int(stack.pop())

            stack.append(operations[item](first, second))

    result = stack.pop()
    return result


values = []
operators = []

while True:
    user_input = input("> ")
    print(user_input)
    if user_input == "q":
        break
    elif len(user_input) > 1:
        print("will handle long string later")
    elif user_input in operations.keys():
        operators.append(user_input)
    else:
        values.append(user_input)

    if len(operators) + 1 == len(values):
        output = calculate(values + operators)
        values = [output]
        operators = []

        if len(values) == 1:
            print(values[0])
