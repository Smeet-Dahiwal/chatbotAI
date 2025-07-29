# ========================================
# Find Factorial of a Number (Multiple Ways)
# ========================================

# ----------------------------------------
# Method 1: Recursive Function
# Logic:
# - A function that calls itself.
# - Base case: factorial of 0 or 1 is 1.
# - Recursive case: n * factorial of (n - 1).
# - It keeps calling itself until it reaches the base case.
# ----------------------------------------
def factorial_recursive(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# ----------------------------------------
# Method 2: Iterative Function (loop)
# Logic:
# - Uses a loop to multiply numbers from 2 to n.
# - Maintains a variable `result` starting at 1.
# - Each number in the loop is multiplied into `result`.
# - Final value of `result` is the factorial.
# ----------------------------------------
def factorial_iterative(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# ----------------------------------------
# Method 3: Using math.factorial (built-in)
# Logic:
# - Uses Python's built-in `math.factorial()` method.
# - Automatically handles computation and error handling.
# - Raises `ValueError` for negative inputs.
# ----------------------------------------
import math
def factorial_builtin(n):
    try:
        return math.factorial(n)
    except ValueError:
        return "Factorial not defined for negative numbers"

# ========================================
# Example Usage
# ========================================
# Ask user to input a number and display factorial using all 3 methods
num = int(input("Enter a number to find factorial: "))

print("\nFactorial (recursive):", factorial_recursive(num))
print("Factorial (iterative):", factorial_iterative(num))
print("Factorial (math.factorial):", factorial_builtin(num))
