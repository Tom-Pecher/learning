
# DSA: W3Schools - Arrays Tutorial
# Section 9: Linear Search

my_array = [7, 3, 9, 12, 11]

# Linear Search Algorithm: O(n)
def linear_search(array, target_val):
    for i in range(len(array)):
        if array[i] == target_val:
            return True, array[i]
    return False, None

print("Sorted array:", linear_search(my_array, 0))
