from RPNCalculator import Calculator

if __name__ == "__main__":
    c = Calculator()

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
