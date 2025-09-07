#!/usr/bin/env python3
# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations on two numbers.

    Args:
        num1: The first number
        num2: The second number
        operation: The operation to perform ('add', 'subtract', 'multiply', 'divide')

    Returns:
        The result of the operation, or an error message for invalid cases
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
