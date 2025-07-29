# ========================================
# Merge Two Sorted Lists (Multiple Ways)
# ========================================

# Two sample sorted lists to merge
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

# ----------------------------------------
# Method 1: Using sorted() after concatenation
# ----------------------------------------
# Logic:
# - Combine both lists using '+' operator.
# - Then use sorted() to sort the combined list.
# - Simple but less efficient for large datasets.
def merge_sorted_concat(lst1, lst2):
    return sorted(lst1 + lst2)

# ----------------------------------------
# Method 2: Using Two-Pointer Technique (Manual Merge)
# ----------------------------------------
# Logic:
# - Use two pointers (indices) to iterate over both lists.
# - Compare elements at each pointer and add the smaller one to the result list.
# - Once one list is exhausted, append the remaining elements from the other.
# - Efficient and commonly used in merge sort.
def merge_sorted_two_pointer(lst1, lst2):
    merged = []
    i = j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged.append(lst1[i])
            i += 1
        else:
            merged.append(lst2[j])
            j += 1
    merged.extend(lst1[i:])  # Append remaining from list1
    merged.extend(lst2[j:])  # Append remaining from list2
    return merged

# ----------------------------------------
# Method 3: Using heapq.merge (Efficient for Large Sorted Inputs)
# ----------------------------------------
# Logic:
# - heapq.merge returns a generator that merges multiple sorted inputs efficiently.
# - Internally uses a heap to always yield the smallest current element.
# - Convert the result to a list if a list is needed.
import heapq
def merge_sorted_heapq(lst1, lst2):
    return list(heapq.merge(lst1, lst2))

# ========================================
# Example Usage
# ========================================

print("List 1:", list1)
print("List 2:", list2)

print("\nMerged using sorted() + concatenation:")
print("Result:", merge_sorted_concat(list1, list2))

print("\nMerged using two-pointer technique:")
print("Result:", merge_sorted_two_pointer(list1, list2))

print("\nMerged using heapq.merge:")
print("Result:", merge_sorted_heapq(list1, list2))
