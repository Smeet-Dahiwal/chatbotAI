# ========================================
# Find Unique Elements from a List
# ========================================

# Sample list
sample_list = [1, 2, 2, 3, 4, 4, 5, 1, 6, 7, 7, 8]

# ----------------------------------------
# Method 1: Using loop and count() method
# Logic:
# - Traverse each element
# - If its count in the list is 1, it's unique
# ----------------------------------------
def find_unique_by_count(lst):
    unique = []
    for item in lst:
        if lst.count(item) == 1:
            unique.append(item)
    return unique

# ----------------------------------------
# Method 2: Using dictionary to count occurrences
# Logic:
# - First, store frequencies of each item in a dictionary
# - Then return items with count = 1
# ----------------------------------------
def find_unique_by_dict(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return [key for key, val in freq.items() if val == 1]

# ----------------------------------------
# Method 3: Using collections.Counter
# Logic:
# - Counter creates a dictionary of element counts
# - Return elements with count = 1
# ----------------------------------------
from collections import Counter
def find_unique_by_counter(lst):
    counter = Counter(lst)
    return [item for item, count in counter.items() if count == 1]

# ----------------------------------------
# Method 4: Using set and list comprehension
# Logic:
# - Similar to Method 1 but written compactly in one line
# ----------------------------------------
def find_unique_by_set(lst):
    return [item for item in lst if lst.count(item) == 1]


# ========================================
# Example Usage for Finding Unique Elements
# ========================================
print("Original List:", sample_list)
print("Unique elements (using count):", find_unique_by_count(sample_list))
print("Unique elements (using dict):", find_unique_by_dict(sample_list))
print("Unique elements (using Counter):", find_unique_by_counter(sample_list))
print("Unique elements (using set/list comp):", find_unique_by_set(sample_list))


# ========================================
# Sort a List of Integers (Ascending and Descending)
# ========================================

# Sample list
sample_list = [5, 2, 9, 1, 5, 6, 3, 7]

# ----------------------------------------
# Method 1: Using sorted() - returns a new sorted list
# Logic:
# - Built-in function
# - Does not modify the original list
# ----------------------------------------
def sort_with_sorted(lst):
    return sorted(lst)  # Ascending by default

# ----------------------------------------
# Method 2: Using sorted() with reverse=True for descending
# Logic:
# - Same as Method 1 but sorted in reverse order
# ----------------------------------------
def sort_with_sorted_descending(lst):
    return sorted(lst, reverse=True)

# ----------------------------------------
# Method 3: Using list.sort() - sorts in-place
# Logic:
# - Built-in method that modifies the original list directly
# ----------------------------------------
def sort_in_place(lst):
    lst.sort()  # modifies the original list
    return lst

# ----------------------------------------
# Method 4: Manual sorting using Bubble Sort
# Logic:
# - Compare adjacent items
# - Swap them if they are in wrong order
# - Repeat n times
# ----------------------------------------
def sort_bubble(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

# ========================================
# Example Usage for Sorting
# ========================================
print("Original List:", sample_list)

# sorted() - creates new sorted list
print("Sorted (sorted()):", sort_with_sorted(sample_list))

# sorted() - descending
print("Sorted Descending (sorted reverse):", sort_with_sorted_descending(sample_list))

# list.sort() - modifies original list
copy_list = sample_list.copy()
print("Sorted (in-place sort()):", sort_in_place(copy_list))

# Bubble Sort
copy_list2 = sample_list.copy()
print("Sorted (bubble sort):", sort_bubble(copy_list2))
