
# DSA: W3Schools - Arrays Tutorial
# Section 10: Binary Search

# For binary search to work, the array must be sorted
my_array = [3, 7, 9, 11, 12]

# Binary Search Algorithm: O(log n) 
def binary_search(array, target_val):
    mid = array[len(array) // 2]

    if mid == target_val:
        return True, mid
    elif len(array) == 1:
        return False, None
    else:
        if target_val < mid:
            return binary_search(array[:len(array) // 2], target_val)
        elif target_val > mid:
            return binary_search(array[len(array) // 2:], target_val)
        else:
            raise ValueError("Condition should not be reached")

print("Sorted array:", binary_search(my_array, 11))
