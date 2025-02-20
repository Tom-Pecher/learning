
# DSA: W3Schools - Arrays Tutorial
# Section 8: Merge Sort

my_array = [7, 3, 9, 12, 11]

# Merge Sort Algorithm: O(n logn)
def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    leftHalf = array[:mid]
    rightHalf = array[mid:]

    sortedLeft = merge_sort(leftHalf)
    sortedRight = merge_sort(rightHalf)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

print("Sorted array:", merge_sort(my_array))
