# Calculator
from art import logo


# Add
def add(n1, n2):
    return n1 + n2


# Substract
def substract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    if n2 == 0:
        return "Invalid number. Division 0"
    return n1 / n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    is_finished = False
    num1 = float(input("What's the first number?: "))

    for key in operations:
        print(key)

    while not is_finished:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        response = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if response == 'y':
            num1 = answer
        else:
            is_finished = True
            calculator()


calculator()
