from RPNCalculator import Calculator


class CommandLineCalculator:
    def __init__(self):
        self.c = Calculator()

    def start(self):
        self.print_instructions()
        while True:
            print("*" * 20)
            print("Calculator: " + str(self.c))
            user_input = input("> ")
            if user_input == "q":
                break
            else:
                result = self.c.input(user_input)
                if "error" in result.lower():
                    print(result)

    def stop(self):
        print("To be implemented")

    def print_instructions(self):
        print("Welcome to the command line RPN Calculator!")
        print("Usage: Add two or more values and then provide an operator.")
        print(
            "Inputs can be one at a time or multiple on one row, separated by a space."
        )
        print("Available operations are " + self.c.get_operations_description())
