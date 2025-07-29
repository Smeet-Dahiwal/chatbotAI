# Program to find duplicate elements in a list using multiple methods
# Each method includes logic explanation as comments

# Sample input list (you can also take user input if needed)
input_list = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 3, 1]

print("Original List:", input_list)

# ------------------ 1. Using Set and Loop ------------------
# Logic: Use a set to track seen elements.
# If an element is already in the set, it is a duplicate.
def find_duplicates_set_loop(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)  # already seen, so it's a duplicate
        else:
            seen.add(item)  # first time seeing the element
    return list(duplicates)

# ------------------ 2. Using Collections.Counter ------------------
# Logic: Count frequency of each element.
# If frequency > 1, it's a duplicate.
from collections import Counter

def find_duplicates_counter(lst):
    counter = Counter(lst)
    return [item for item, count in counter.items() if count > 1]

# ------------------ 3. Using List Comprehension and Count() ------------------
# Logic: Check if element count > 1.
# Only include if not already added to result.
def find_duplicates_listcomp(lst):
    duplicates = []
    for item in lst:
        if lst.count(item) > 1 and item not in duplicates:
            duplicates.append(item)
    return duplicates

# ------------------ 4. Using Dictionary ------------------
# Logic: Track occurrences using a dictionary.
# Add to result if count reaches 2.
def find_duplicates_dict(lst):
    freq = {}
    duplicates = []
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
        if freq[item] == 2:  # Add only once when it becomes a duplicate
            duplicates.append(item)
    return duplicates

# ------------------ 5. Using Set Comprehension (One-liner) ------------------
# Logic: Use set to keep track of seen items and another to collect duplicates
def find_duplicates_oneliner(lst):
    seen = set()
    return list({x for x in lst if x in seen or seen.add(x)})

# ------------------ Run All Methods ------------------

print("\n--- Duplicate Elements Using Multiple Methods ---\n")
print("1. Using Set + Loop:         ", find_duplicates_set_loop(input_list))
print("2. Using Counter:            ", find_duplicates_counter(input_list))
print("3. Using List Comprehension: ", find_duplicates_listcomp(input_list))
print("4. Using Dictionary:         ", find_duplicates_dict(input_list))
print("5. One-liner Set Logic:      ", find_duplicates_oneliner(input_list))
