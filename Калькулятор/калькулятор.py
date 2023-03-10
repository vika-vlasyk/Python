def add(n1, n2):
    """Compute and return the sum of two numbers."""
    return n1 + n2


def subtract(n1, n2):
    """Compute and return the difference of two numbers."""
    return n1 - n2


def multiply(n1, n2):
    """Compute and return the multiply of two numbers."""
    return n1 * n2


def divide(n1, n2):
    """Compute and return the divide of two numbers."""

    return n1 / n2


def remainder(n1, n2):
    return n1 % n2


def divide_int(n1, n2):
    """Compute and return the divide of two numbers int."""
    result = int(n1) / int(n2)
    return result


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    ":": divide,
    "%": remainder,
    "/": divide_int,
}


def calculator():

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if (
            input(
                f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: "
            )
            == "y"
        ):
            num1 = answer
        else:
            should_continue = False

            calculator()


calculator()
