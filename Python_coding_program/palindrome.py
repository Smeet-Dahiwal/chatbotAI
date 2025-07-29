# =========================
# 1. Reverse a String
# =========================

# Method 1: Using slicing
def reverse_string_slicing(s):
    # Pythonic and fastest way using slicing [start:stop:step]
    return s[::-1]

# Method 2: Using loop
def reverse_string_loop(s):
    # Loop through each character and prepend to result
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# Method 3: Using reversed() and join()
def reverse_string_builtin(s):
    # reversed() returns an iterator, join combines characters into a string
    return ''.join(reversed(s))


# =========================
# 2. Reverse an Integer
# =========================

# Method 1: Convert to string
def reverse_integer_string(n):
    # Determine sign, reverse string of absolute number, then restore sign
    sign = -1 if n < 0 else 1
    reversed_num = int(str(abs(n))[::-1])
    return sign * reversed_num

# Method 2: Using while loop (math logic)
def reverse_integer_math(n):
    # Extract digits and build reversed number using modulus and division
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_num = 0
    while n != 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return sign * reversed_num


# =========================
# 3. Check if a String is Palindrome
# =========================

# Method 1: Using slicing
def is_palindrome_slicing(s):
    # A palindrome reads same forwards and backwards
    return s == s[::-1]

# Method 2: Using loop
def is_palindrome_loop(s):
    # Compare characters from both ends moving toward center
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True

# Method 3: Ignoring case and spaces
def is_palindrome_cleaned(s):
    # Remove non-alphanumeric characters and convert to lowercase
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]


# =========================
# 4. Count Occurrences of a Character
# =========================

# Method 1: Using built-in count()
def count_char_builtin(s, ch):
    # count() returns number of times character appears in string
    return s.count(ch)

# Method 2: Using loop
def count_char_loop(s, ch):
    # Manually count matching characters
    count = 0
    for c in s:
        if c == ch:
            count += 1
    return count

# Method 3: Using collections.Counter
from collections import Counter
def count_char_counter(s, ch):
    # Counter returns a dictionary of character frequencies
    return Counter(s)[ch]


# =========================
# Example Usage
# =========================

# Reverse string
user_string = input("Enter a string to reverse: ")
print("Reversed (slicing):", reverse_string_slicing(user_string))
print("Reversed (loop):", reverse_string_loop(user_string))
print("Reversed (builtin):", reverse_string_builtin(user_string))

# Reverse integer
user_int = int(input("\nEnter an integer to reverse: "))
print("Reversed integer (string):", reverse_integer_string(user_int))
print("Reversed integer (math):", reverse_integer_math(user_int))

# Palindrome check
pal_str = input("\nEnter a string to check palindrome: ")
print("Is Palindrome (slicing)?", is_palindrome_slicing(pal_str))
print("Is Palindrome (loop)?", is_palindrome_loop(pal_str))
print("Is Palindrome (cleaned)?", is_palindrome_cleaned(pal_str))

# Count occurrences
count_str = input("\nEnter a string: ")
count_ch = input("Enter a character to count: ")
print(f"Occurrences (builtin) of '{count_ch}':", count_char_builtin(count_str, count_ch))
print(f"Occurrences (loop) of '{count_ch}':", count_char_loop(count_str, count_ch))
print(f"Occurrences (Counter) of '{count_ch}':", count_char_counter(count_str, count_ch))
