# ================================
# Remove Duplicates from a List
# ================================

# Sample list
sample_list = [1, 2, 2, 3, 4, 4, 5, 1, 6]

# --------------------------------
# Method 1: Using set() (Unordered)
# --------------------------------
def remove_duplicates_set(lst):
    # Convert list to set to remove duplicates (sets only store unique values)
    # Then convert it back to list — this does not preserve original order
    return list(set(lst))

# --------------------------------
# Method 2: Using loop (Preserve order)
# --------------------------------
def remove_duplicates_loop(lst):
    unique = []
    for item in lst:
        if item not in unique:
            # If the item is not already in the unique list, append it
            unique.append(item)
    return unique  # Preserves the order of first occurrence

# --------------------------------
# Method 3: Using dict.fromkeys() (Preserves order from Python 3.7+)
# --------------------------------
def remove_duplicates_dict(lst):
    # Convert the list to a dictionary using fromkeys
    # Keys in a dictionary are unique, so duplicates are removed
    # Order is preserved in Python 3.7+
    return list(dict.fromkeys(lst))

# --------------------------------
# Method 4: Using list comprehension
# --------------------------------
def remove_duplicates_list_comp(lst):
    seen = []
    # For each element, if not in 'seen', add it to both the result list and 'seen'
    return [seen.append(x) or x for x in lst if x not in seen]
    # 'seen.append(x) or x' ensures x is returned after appending

# --------------------------------
# Method 5: Using collections.OrderedDict (for older Python < 3.7)
# --------------------------------
from collections import OrderedDict
def remove_duplicates_ordered_dict(lst):
    # OrderedDict preserves the insertion order and keeps only the first occurrence of each item
    return list(OrderedDict.fromkeys(lst))

# ================================
# Example Usage
# ================================

print("Original List:", sample_list)

# Using set
print("Without duplicates (set):", remove_duplicates_set(sample_list))  # Not ordered

# Using loop
print("Without duplicates (loop):", remove_duplicates_loop(sample_list))

# Using dict.fromkeys()
print("Without duplicates (dict.fromkeys):", remove_duplicates_dict(sample_list))

# Using list comprehension
print("Without duplicates (list comp):", remove_duplicates_list_comp(sample_list))

# Using OrderedDict
print("Without duplicates (OrderedDict):", remove_duplicates_ordered_dict(sample_list))
