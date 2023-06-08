from operations import operations


class Calculator:
    stack = []

    def __init__(self, ops=operations) -> None:
        self.operations = ops

    def __repr__(self) -> str:
        return " ".join(str(i) for i in self.stack)

    def handle_value(self, val):
        self.stack.append(float(val))

    def handle_operator(self, op):
        return self.calculate(op)

    def handle_complex_input(self, input_string):
        inputs = input_string.split(" ")
        result = ""
        for val in inputs:
            result = self.input(val)

        return result

    def clear(self):
        self.stack = []

    def validate_input_value(self, val):
        try:
            float(val)
            return True
        except:
            return False

    def input(self, value):
        if type(value) == str and value.lower() == "c":
            self.clear()
            return "Cleared"
        elif len(value.split(" ")) > 1:
            return self.handle_complex_input(value)
        elif value in self.operations.keys():
            return self.handle_operator(value)
        else:
            if self.validate_input_value(value):
                self.handle_value(value)
                return value
            else:
                self.clear()
                return "Your input contained an error, please start over."

    def calculate(self, operator):
        second = self.stack.pop()
        first = self.stack.pop()

        result = self.operations[operator](first, second)
        self.handle_value(result)
        return result
