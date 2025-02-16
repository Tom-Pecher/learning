
# DSA: W3Schools - Arrays Tutorial
# Section 4: Insertion Sort

my_array = [7, 3, 9, 12, 11]

# Insertion Sort Algorithm: O(n^2)
def insertion_sort(my_array):
    n = len(my_array)
    for i in range(1,n):
        insert_index = i
        current_value = my_array.pop(i)
        for j in range(i-1, -1, -1):
            if my_array[j] > current_value:
                insert_index = j
        my_array.insert(insert_index, current_value)
    return my_array

print("Sorted array:", insertion_sort(my_array))
