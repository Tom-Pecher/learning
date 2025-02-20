
# DSA: W3Schools - Arrays Tutorial
# Section 9: Linear Search

my_array = [7, 3, 9, 12, 11]

# Linear Search Algorithm: O(n)
def linear_search(arr, targetVal):
    for i in range(len(arr)):
        if arr[i] == targetVal:
            return True, arr[i]
    return (False, None)

print("Sorted array:", linear_search(my_array, 9))
