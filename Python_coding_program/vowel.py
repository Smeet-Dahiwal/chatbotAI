# =====================================================
# Program: Count Vowels and Consonants in a String
# Description:
#   This program demonstrates multiple methods to count
#   vowels and consonants from a given input string.
#   It handles:
#   - Only alphabetic characters (ignores digits/punctuation)
#   - Both lowercase and uppercase letters
# =====================================================

sample_text = "Hello, World!"

# -----------------------------------------------------
# Method 1: Using a loop and set for vowels
# Logic:
#   - Use a set of vowels for quick lookup.
#   - Loop through each character in the text.
#   - If the character is an alphabet:
#       - Check if it's a vowel or consonant.
#   - Increment counts accordingly.
# -----------------------------------------------------
def count_vowels_consonants_loop(text):
    vowels = set("aeiouAEIOU")  # Set for fast lookup
    vowel_count = 0
    consonant_count = 0
    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count

# -----------------------------------------------------
# Method 2: Using list comprehensions
# Logic:
#   - Filter only alphabet characters.
#   - Use list comprehension to count vowels.
#   - Subtract vowel count from total alphabet count 
#     to get consonant count.
# -----------------------------------------------------
def count_vowels_consonants_lc(text):
    vowels = set("aeiouAEIOU")
    text_alpha = [char for char in text if char.isalpha()]  # Keep only alphabets
    vowel_count = sum(1 for char in text_alpha if char in vowels)
    consonant_count = len(text_alpha) - vowel_count
    return vowel_count, consonant_count

# -----------------------------------------------------
# Method 3: Using collections.Counter (case-insensitive)
# Logic:
#   - Convert all alphabetic characters to lowercase.
#   - Use Counter to count frequency of each character.
#   - Sum counts of vowel keys for vowels.
#   - Sum remaining alphabet keys as consonants.
# -----------------------------------------------------
from collections import Counter

def count_vowels_consonants_counter(text):
    vowels = set("aeiou")  # lowercase only for matching
    filtered_text = [char.lower() for char in text if char.isalpha()]
    counter = Counter(filtered_text)
    vowel_count = sum(counter[char] for char in vowels)
    consonant_count = sum(counter[char] for char in counter if char not in vowels)
    return vowel_count, consonant_count

# =====================================================
# Example Usage
# =====================================================
print("Sample Text:", sample_text)

v1, c1 = count_vowels_consonants_loop(sample_text)
print("Method 1 (loop):", f"Vowels = {v1}, Consonants = {c1}")

v2, c2 = count_vowels_consonants_lc(sample_text)
print("Method 2 (list comprehension):", f"Vowels = {v2}, Consonants = {c2}")

v3, c3 = count_vowels_consonants_counter(sample_text)
print("Method 3 (Counter):", f"Vowels = {v3}, Consonants = {c3}")
