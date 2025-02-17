
# DSA: W3Schools - Arrays Tutorial
# Section 6: Counting Sort

# Counting sort is a niche algorithm that requires several conditions to be met:
    # Elements must be integers
    # Elements must be within a specific range
    # Elements must be non-negative
my_array = [7, 3, 9, 12, 11]

# Counting Sort Algorithm: O(n^2) but in general O(n+k) where k is the range of values:
def counting_sort(array):
    max_val = max(array)
    count = [0] * (max_val + 1)

    while len(array) > 0:
        num = array.pop(0)
        count[num] += 1

    for i in range(len(count)):
        while count[i] > 0:
            array.append(i)
            count[i] -= 1

    return array

print("Sorted array:", counting_sort(my_array))
