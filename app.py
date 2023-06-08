from calculator import Calculator


def divide(val1, val2):
    print("custom divide!")
    return round(val1 / val2, 5)


def power(val1, val2):
    return val1**val2


def greater(val1, val2):
    if val2 > val1:
        return val2
    else:
        return val1


operations = {"/": divide, "^": power, ">": greater}


c = Calculator(operations)

while True:
    print("*" * 12)
    print("Calculator: " + str(c))
    user_input = input("> ")
    if user_input == "q":
        break
    else:
        result = c.input(user_input)
        if "error" in result.lower():
            print(result)
