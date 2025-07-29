# ========================================
# Find the Second Largest Element in a List
# ========================================
# Logic:
# This script finds the second largest unique element in a list.
# - Method 1: Sorts the list in descending order after removing duplicates, then returns the second element.
# - Method 2: Traverses the list once, tracking the largest and second largest values efficiently.
# - Method 3: Uses heapq.nlargest to get the top two largest unique elements and returns the second one.

# Sample list
sample_list = [10, 20, 4, 45, 99, 99, 7]

# ----------------------------------------
# Method 1: Using sorting (descending)
# ----------------------------------------
def second_largest_sorted(lst):
    unique = list(set(lst))  # Remove duplicates
    if len(unique) < 2:
        return "List doesn't have a second largest element"
    unique.sort(reverse=True)
    return unique[1]

# ----------------------------------------
# Method 2: One-pass scan (efficient)
# ----------------------------------------
def second_largest_one_pass(lst):
    if len(lst) < 2:
        return "List too short"
    first = second = float('-inf')
    for num in lst:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else "No second largest element"

# ----------------------------------------
# Method 3: Using heapq.nlargest (built-in)
# ----------------------------------------
import heapq
def second_largest_heapq(lst):
    unique = list(set(lst))  # Remove duplicates
    if len(unique) < 2:
        return "No second largest element"
    return heapq.nlargest(2, unique)[1]

# ========================================
# Example Usage
# ========================================

print("Original list:", sample_list)

print("Second largest (sorted):", second_largest_sorted(sample_list))
print("Second largest (one pass):", second_largest_one_pass(sample_list))
print("Second largest (heapq):", second_largest_heapq(sample_list))
