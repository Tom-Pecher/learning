
# DSA: W3Schools - Arrays Tutorial
# Section 3: Selection Sort

my_array = [7, 3, 9, 12, 11]

# Selection Sort Algorithm: O(n^2)
def selection_sort(my_array):
    n = len(my_array)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if my_array[j] < my_array[min_index]:
                min_index = j   
        my_array[i], my_array[min_index] = my_array[min_index], my_array[i]
    return my_array

print("Sorted array:", selection_sort(my_array))
