# ========================================
# Check if Two Strings Are Anagrams
# ========================================

# -------------------- LOGIC --------------------
# Anagrams are strings with the same characters in the same frequency, but possibly in different orders.
# There are multiple ways to check for anagrams:
# 1. Sort both strings and compare the sorted results.
# 2. Use collections.Counter to compare character frequencies.
# 3. Use a manual dictionary to count character occurrences.
# Each method ensures that both strings contain exactly the same characters the same number of times.
# -----------------------------------------------

# Sample input
str1 = "listen"
str2 = "silent"

# ----------------------------------------
# Method 1: Sort both strings and compare
# ----------------------------------------
def are_anagrams_sort(s1, s2):
    # Remove spaces and convert to lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)

# ----------------------------------------
# Method 2: Use collections.Counter
# ----------------------------------------
from collections import Counter

def are_anagrams_counter(s1, s2):
    # Clean and compare letter frequencies
    return Counter(s1.replace(" ", "").lower()) == Counter(s2.replace(" ", "").lower())

# ----------------------------------------
# Method 3: Manual count using dictionary
# ----------------------------------------
def are_anagrams_manual(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2):
        return False

    count_dict = {}

    for char in s1:
        count_dict[char] = count_dict.get(char, 0) + 1

    for char in s2:
        if char not in count_dict:
            return False
        count_dict[char] -= 1
        if count_dict[char] < 0:
            return False

    return True

# ========================================
# Example Usage
# ========================================
print(f"String 1: {str1}")
print(f"String 2: {str2}")

print("Method 1 (Sort):", are_anagrams_sort(str1, str2))            # ✅ True
print("Method 2 (Counter):", are_anagrams_counter(str1, str2))      # ✅ True
print("Method 3 (Manual Count):", are_anagrams_manual(str1, str2))  # ✅ True
