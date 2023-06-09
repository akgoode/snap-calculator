from RPNCalculator import Calculator


class Shutdown(Exception):
    pass


class CommandLineCalculator:
    def __init__(self):
        self.c = Calculator()

    def start(self):
        try:
            self.print_instructions()
            while True:
                print("*" * 20)
                print("Calculator: " + str(self.c))
                user_input = input("> ")
                if user_input == "q":
                    raise Shutdown
                else:
                    result = self.c.input(user_input)
                    if "error" in result.lower():
                        print(result)
        except Shutdown:
            self.stop("User initiated shutdown.  Exiting.")
        except EOFError:
            self.stop("\nReceived end of file.  Exiting.")
        except KeyboardInterrupt:
            self.stop("\nReceived keyboard interrupt.  Exiting.")
        except:
            self.stop("Unexpected error occurred. Exiting.")

    def stop(self, message):
        print(message)
        exit()

    def print_instructions(self):
        print("Welcome to the command line RPN Calculator!")
        print("Usage: Add two or more values and then provide an operator.")
        print(
            "Inputs can be one at a time or multiple on one row, separated by a space."
        )
        print("Available operations are " + self.c.get_operations_description())
