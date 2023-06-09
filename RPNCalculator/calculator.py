def multiply(val1, val2):
    return val1 * val2


def add(val1, val2):
    return val1 + val2


def subtract(val1, val2):
    return val1 - val2


def divide(val1, val2):
    return round(val1 / val2, 3)


defaults = {"*": multiply, "+": add, "-": subtract, "/": divide}


class Calculator:
    stack = []

    def __init__(self, ops=defaults) -> None:
        if ops is defaults:
            self.operations = ops
        else:
            self.operations = defaults | ops

    def __repr__(self) -> str:
        if len(self.stack) == 0:
            return "[ ]"
        else:
            values = " ".join(str(i) for i in self.stack)
            return f"[ {values} ]"

    def get_operations_description(self):
        return " ".join(i for i in self.operations)

    def clear(self):
        self.stack = []

    def input(self, value) -> str:
        try:
            if type(value) == str and value.lower() == "c":
                self.clear()
                return "Cleared"
            elif len(value.split(" ")) > 1:
                return str(self.__handle_complex_input(value))
            elif value in self.operations.keys():
                return str(self.__handle_operator(value))
            else:
                if self.__validate_input_value(value):
                    self.__handle_value(value)
                    return str(value)
                else:
                    self.clear()
                    return "Error: Bad input, please start over."
        except:
            return "Error: please start over."

    def __handle_value(self, val):
        self.stack.append(float(val))

    def __handle_operator(self, op):
        return self.__calculate(op)

    def __handle_complex_input(self, input_string):
        inputs = input_string.split(" ")
        result = ""
        for val in inputs:
            result = self.input(val)

        return result

    def __validate_input_value(self, val):
        try:
            float(val)
            return True
        except:
            return False

    def __calculate(self, operator):
        try:
            second = self.stack.pop()
            first = self.stack.pop()
        except:
            self.clear()
            return "Error: Invalid sequence, please start over."

        result = self.operations[operator](first, second)
        self.__handle_value(result)
        return result
