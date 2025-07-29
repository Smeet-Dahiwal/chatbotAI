# ========================================
# Reverse a String in Python (Multiple Ways)
# ========================================

# ----------------------------------------
# Method 1: Using slicing
# ----------------------------------------
text = "hello"

# Slicing syntax [::-1] means:
# - Start from the end of the string and move backwards by 1 step
# - This effectively reverses the string
reversed_text = text[::-1]

print("Reversed string (slicing):", reversed_text)

# ----------------------------------------
# Method 2: Using a loop
# ----------------------------------------
text = "hello"
reversed_text = ""

# Loop through each character in the string
for char in text:
    # Prepend each character to the result (new string starts with the current char)
    reversed_text = char + reversed_text

print("Reversed string (loop):", reversed_text)

# ----------------------------------------
# Method 3: Using reversed() and join()
# ----------------------------------------
text = "hello"

# reversed(text) returns a reverse iterator over the string
# ''.join(...) joins the characters from the reversed iterator into a single string
reversed_text = ''.join(reversed(text))

print("Reversed string (reversed + join):", reversed_text)
