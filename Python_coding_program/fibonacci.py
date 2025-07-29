# ========================================
# Generate Fibonacci Sequence (Multiple Ways)
# ========================================

# ----------------------------------------
# Method 1: Iterative Function
# ----------------------------------------
# Logic:
# - If n <= 0: Return an empty list.
# - If n == 1: Only return [0] as the sequence.
# - Initialize a list with first two Fibonacci numbers: [0, 1]
# - From index 2 to n, keep appending sum of last two numbers to the list.
def fibonacci_iterative(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])  # last + second last
    return sequence

# ----------------------------------------
# Method 2: Recursive Function (Not recommended for large n)
# ----------------------------------------
# Logic:
# - Base case: if n <= 0, return empty list.
# - Use a helper recursive function `fib(i)`:
#   - fib(0) = 0, fib(1) = 1
#   - fib(n) = fib(n-1) + fib(n-2)
# - Generate list using list comprehension: [fib(0), fib(1), ..., fib(n-1)]
# - Note: Inefficient for large `n` due to repeated computations.
def fibonacci_recursive(n):
    if n <= 0:
        return []
    def fib(i):
        if i <= 1:
            return i
        return fib(i - 1) + fib(i - 2)
    return [fib(i) for i in range(n)]

# ----------------------------------------
# Method 3: Generator Function (memory-efficient)
# ----------------------------------------
# Logic:
# - Use a generator to yield one Fibonacci number at a time.
# - Start with a = 0, b = 1
# - In each iteration:
#   - yield a
#   - a becomes b, b becomes a + b
# - Continue for `n` terms.
def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# ========================================
# Example Usage
# ========================================

num = int(input("Enter number of Fibonacci terms: "))

print("\nFibonacci (iterative):", fibonacci_iterative(num))
print("Fibonacci (recursive):", fibonacci_recursive(num))
print("Fibonacci (generator):", list(fibonacci_generator(num)))
