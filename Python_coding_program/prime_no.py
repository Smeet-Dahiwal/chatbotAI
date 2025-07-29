# ============================================
# Print all prime numbers up to N
# ============================================
# A prime number is a number greater than 1 that has no divisors other than 1 and itself.
# To check if a number is prime:
# - Basic method: Try dividing it by all numbers from 2 to n-1.
# - Optimized: Divide only up to sqrt(n).
# - Sieve of Eratosthenes: Efficient way to find all primes ≤ N.

# Input
N = 50

# --------------------------------------------
# Method 1: Basic approach
# --------------------------------------------
def print_primes_basic(n):
    print("\nMethod 1: Basic Approach")
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=' ')

# --------------------------------------------
# Method 2: Optimized check (up to sqrt(n))
# --------------------------------------------
import math
def print_primes_optimized(n):
    print("\n\nMethod 2: Optimized (sqrt(n))")
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=' ')

# --------------------------------------------
# Method 3: Sieve of Eratosthenes
# --------------------------------------------
def print_primes_sieve(n):
    print("\n\nMethod 3: Sieve of Eratosthenes")
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    for i in range(2, n + 1):
        if is_prime[i]:
            print(i, end=' ')

# --------------------------------------------
# Call all methods
# --------------------------------------------
print(f"Prime numbers up to {N}:\n")
print_primes_basic(N)
print_primes_optimized(N)
print_primes_sieve(N)
