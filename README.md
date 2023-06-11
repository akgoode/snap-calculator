# Reverse Polish Notation Calculator

## Purpose

A command line Reverse Polish Notation calculator that is built to be extensible and consumable by a variety of different services and in different applications.

The application available to run here is a simple wrapper around the RPNCalculator package which allows for continuous input through the command line, and decorates the input and output a little bit more for a better user experience than the raw package.

## Setup

1. Clone this repo
2. Run `python3 app.py`
3. Enter inputs

## Testing

1. From the root, run `python3 -m unittest`

## Architecture

This application consists of 2 packages, a command line application that passes inputs to the calculator class, and the calculator class which manages the input and returns outcomes of users' inputs, whether valid or invalid.

## Usage

This calculator was designed to be compatible with multiple input methods: one number or operation at a time, a sequence of values, or a combination.

The calculator class itself has a simple API, a function called `input` and a function called `get_operations_description`. `input` receives a string and returns a string. The input string can be a numerical value, an operator, or a valid RPN sequence. The user can change between input types, for instance entering first a long sequence, then another value and operator. `get_operations_description` will return a string that contains all valid operations that have been configured for the calculator at startup.

In the event that a user enters a sequence of characters, the calculator will add them in sequence as if they were entered individually, also taking into account any values that might be stored in memory.

Some additional values are:

1.  'q' will quit the application.
2.  'c' or 'C' will clear the memory of the calculator.

The output string will depend on that the most recent input is. In the event of a value being entered, the application will output that value. If the input is an operator and there are at least 2 values stored in memory, the output will be the result of that operation. If the input is a sequence of values, the output will be whatever the resulting output would have been if it was a single input.

Some examples of valid inputs:

```
> 2
2
> 5
5
> +
7.0
```

```
> 2 5 +
7.0
```

```
> 2 5
5
> +
7.0
```

```
> 5 5 5 8 + + -
-13.0
> 13 +
0.0
```

```
> 2
2
> c
Cleared
```

Some examples of invalid inputs:

```
> +
Error: Invalid sequence, please start over.
```

```
> 5 2 3 1 + - / *
Error: Invalid sequence, please start over.
```

```
> a
Error: Bad input, please start over.
```

Additionally, printing or otherwise using the calculator as a string will result in a string that describes the current set of values on its stack. This is useful for presenting a good user interface for consumption by 3rd parties.

The command line version of this app adds a little more visibility into the current state of the calculator using this feature. When starting the app, it will show an empty calculator object and a dividing line. When the user enters a value, it will appear in the calculator object. When the user enters an operator, the operation will occur and the calculator will update to show the resulting value in the calculator. This was a design choice to make this particular implementation of the calculator a bit more user-friendly to someone who may be inputting values on the command line, and was implemented outside of the calculator class. The API of the calculator itself only takes in values and returns values or errors, and leaves this part up to the implementation.

Some examples of the command line wrapper around the calculator:

```
************
Calculator: [ ]
> 2
************
Calculator: [ 2.0 ]
> 5
************
Calculator: [ 2.0 5.0 ]
> +
************
Calculator: [ 7.0 ]
> c
************
Calculator: [ ]
>
```

```
************
Calculator: [ ]
> +
Error: Invalid sequence, please start over.
************
Calculator: [ ]
>
```

```
************
Calculator: [ ]
> 5 5 2 + - -
Error: Invalid sequence, please start over.
************
Calculator: [ ]
>
```

## Extensibility

By default, the calculator will contain the operations for addition, subtraction, multiplication, and division. When creating an instance of the calculator class, the consumer can also pass in a dictionary of operations for it to use. The keys of this dictionary are the string values of the operations themselves, and the values are the functions that will get called.

At the moment, each function must adhere to this signature:

`(val1: float, val2: float) -> float`

This dictionary will be merged with the default operation dictionary, so in the event that the default operations need to be overwritten, they can be passed with the corresponding symbol.

Here is an example of this in action:

```python
def divide(val1, val2):
    print("custom divide!")
    return round(val1 / val2, 5)


def power(val1, val2):
    return val1**val2


operations = {"/": divide, "^": power}

calc = Calculator(operations)
```

The result of instantiating the calculator like this will be that the default addition, subtraction, and multiplication functions will be used, the divide function will be overwritten by this custom division function, and the calculator will have the newly implemented "power" function available with the operator `^`.

This also allows for some other creative operations that aren't traditionally done on a calculator. We can modify the last example to do something like this:

```python
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
```

Now there is a `greater` function which will return whichever of the 2 operands is larger, or just the first value if they are equal.

## Next Steps and Roadmap

1. Features
   - More robust input validation
   - Accept a more robust custom operations dictionary where a consumer of the package can include tests.
   - More options for the end user upon startup (debug mode, default number of decimal places to round, etc.)
   - Support for operations that require 3 inputs
   - Define a calculator interface and allow calculators of different types to be used
2. Deployment
   - Publish RPNCalculator as Pip package.
   - Publish this app on APT for simple install
3. Architecture
   - Dependency injection to decouple the classes from each other.
