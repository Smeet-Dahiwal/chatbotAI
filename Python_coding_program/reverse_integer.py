# =====================================
# Reverse Integer (Positive and Negative)
# =====================================

# --------------------------
# Method 1: Convert to string, reverse, convert back
# --------------------------

num = 12345
# Convert number to string, reverse using slicing, convert back to integer
reversed_num = int(str(num)[::-1])
print("Reversed integer:", reversed_num)

#  If the number is negative:
num = -12345
# str(num)[:0:-1] skips the negative sign, reverses digits only, then multiply by -1
reversed_num = int(str(num)[:0:-1]) * -1
print("Reversed integer:", reversed_num)

# --------------------------
# Method 2: Using while loop (math logic)
# --------------------------

num = 12345
reversed_num = 0

# Extract digits from end using modulus and build reversed number
while num > 0:
    digit = num % 10  # get last digit
    reversed_num = reversed_num * 10 + digit  # shift and add digit
    num //= 10  # remove last digit

print("Reversed integer:", reversed_num)

# If the number is negative:
num = -12345
temp = abs(num)  # make number positive for processing
reversed_num = 0

while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10

reversed_num = -reversed_num  # reapply negative sign
print("Reversed integer:", reversed_num)

# =====================================
# Reverse String
# =====================================

# --------------------------
# Function 1: Using slicing
# --------------------------
def reverse_string_slicing(s):
    # Slice the string from end to start
    return s[::-1]

user_input = input("Enter a string: ")
print("Reversed (slicing):", reverse_string_slicing(user_input))


# --------------------------
# Function 2: Using loop
# --------------------------
def reverse_string_loop(s):
    reversed_str = ""
    # Prepend each character to build reversed string
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

user_input = input("Enter a string: ")
print("Reversed (loop):", reverse_string_loop(user_input))


# --------------------------
# Function 3: Using reversed() and join()
# --------------------------
def reverse_string_builtin(s):
    # reversed() returns an iterator, join() combines into string
    return ''.join(reversed(s))

user_input = input("Enter a string: ")
print("Reversed (built-in):", reverse_string_builtin(user_input))
