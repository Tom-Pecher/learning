
# DSA: W3Schools - Arrays Tutorial
# Section 5: Quick Sort

my_array = [7, 3, 9, 12, 11]

# Quick Sort Algorithm: O(n logn)
def quick_sort(array, low=0, high=None):
    def partition(array, low, high):
        pivot = array[high]
        i = low - 1

        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]

        array[i+1], array[high] = array[high], array[i+1]
        return i+1

    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quick_sort(array, low, pivot_index-1)
        quick_sort(array, pivot_index+1, high)
    return array

print("Sorted array:", quick_sort(my_array))
