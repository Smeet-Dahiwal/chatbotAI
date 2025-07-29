# Program to check if a number is prime using multiple methods
# Each method is explained with logic in comments

import math

# ------------------ 1. Basic Method ------------------
# Logic: Check if number is divisible by any number from 2 to n-1.
def is_prime_basic(n):
    if n <= 1:
        return False  # 0 and 1 are not prime
    for i in range(2, n):
        if n % i == 0:
            return False  # Found a divisor, not prime
    return True  # No divisors found, number is prime

# ------------------ 2. Optimized Method ------------------
# Logic: Instead of checking till n-1, check only up to square root of n.
def is_prime_optimized(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False  # Found a divisor, not prime
    return True

# ------------------ 3. Using all() and List Comprehension ------------------
# Logic: Use Python's all() to check all conditions in one line.
def is_prime_all(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1))

# ------------------ 4. Recursive Method ------------------
# Logic: Use recursion to check divisibility starting from 2 up to √n.
def is_prime_recursive(n, divisor=2):
    if n <= 1:
        return False
    if divisor > int(n ** 0.5):
        return True
    if n % divisor == 0:
        return False
    return is_prime_recursive(n, divisor + 1)

# ------------------ 5. User Input Based Prime Check ------------------
# Logic: Combine input and check using optimized method.
def is_prime_input(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# ------------------ Test the functions ------------------

num = int(input("Enter a number to check if it's prime: "))

print("\n--- Prime Number Check Using Multiple Methods ---\n")
print("1. Basic Method:        ", "Prime" if is_prime_basic(num) else "Not Prime")
print("2. Optimized Method:    ", "Prime" if is_prime_optimized(num) else "Not Prime")
print("3. Using all():         ", "Prime" if is_prime_all(num) else "Not Prime")
print("4. Recursive Method:    ", "Prime" if is_prime_recursive(num) else "Not Prime")
print("5. User Input Method:   ", "Prime" if is_prime_input(num) else "Not Prime")
