
# DSA: W3Schools - Arrays Tutorial
# Section 2: Bubble Sort

my_array = [7, 3, 9, 12, 11]

# Bubble Sort Algorithm: O(n^2)
def bubble_sort(my_array):
    n = len(my_array)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if my_array[j] > my_array[j+1]:
                my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
                swapped = True
        if not swapped:
            break
    return my_array

print("Sorted array:", bubble_sort(my_array))
