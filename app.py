from RPNCalculator import Calculator

if __name__ == "__main__":
    c = Calculator()

    print("Welcome to the command line RPN Calculator!")
    print("Usage: Add two or more values and then provide an operator.")
    print("Inputs can be one at a time or multiple on one row, separated by a space.")
    print("Available operations are " + c.get_operations_description())

    while True:
        print("*" * 20)
        print("Calculator: " + str(c))
        user_input = input("> ")
        if user_input == "q":
            break
        else:
            result = c.input(user_input)
            if "error" in result.lower():
                print(result)
