"""
Calculator Module - Basic arithmetic operations
Students will extend this with more functions
"""


def add(a, b):
    """Add two numbers together"""
    return a + b


def subtract(a, b):
    """Subtract b from a"""
    return a - b


# def multiply(a, b):
#     """Multiply two numbers with input validation and logging."""
#     if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
#         raise TypeError("Both arguments must be numbers")

#     print(f"Multiplying {a} × {b}")  # Added logging
#     result = a * b
#     print(f"Result: {result}")
#     return result

# def divide(a, b):
#     """Divide a by b with enhanced error handling."""
#     if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
#         raise TypeError("Division requires numeric inputs")
#     if b == 0:
#         raise ValueError(f"Cannot divide {a} by zero - division by zero is undefined")


#     print(f"Dividing {a} ÷ {b}")  # Added logging
#     result = a / b
#     print(f"Result: {result}")
#     return result
def multiply(a, b):
    """Multiply two numbers with input validation and logging."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")

    # NOTE: Remove print statements if you don't want terminal output
    # print(f"Multiplying {a} × {b}")
    result = a * b
    # print(f"Result: {result}")
    return result


def divide(a, b):
    """Divide a by b with enhanced error handling."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Division requires numeric inputs")
    if b == 0:
        raise ValueError(f"Cannot divide {a} by zero - division by zero is undefined")

    # NOTE: Remove print statements if you don't want terminal output
    # print(f"Dividing {a} ÷ {b}")
    result = a / b
    # print(f"Result: {result}")
    return result


def power(a, b):
    """Raise a to the power of b"""
    return a**b


def square_root(a):
    """Calculate square root of a"""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return a**0.5


if __name__ == "__main__":
    print("🧮 Calculator Module")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
