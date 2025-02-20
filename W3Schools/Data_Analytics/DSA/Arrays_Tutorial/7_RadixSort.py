
# DSA: W3Schools - Arrays Tutorial
# Section 6: Counting Sort

# A radix is the number of unique digits in a number system (the base).
my_array = [7, 3, 9, 12, 11]

# Radix Sort Algorithm: O(nk) where k is the number of digits in the largest number
def radixSort(array):
    radixArray = [[], [], [], [], [], [], [], [], [], []] # Buckets to store values of each corresponding digit
    maxVal = max(array)
    exp = 1

    while maxVal // exp > 0:

        while len(array) > 0:
            val = array.pop()
            radixIndex = (val // exp) % 10
            radixArray[radixIndex].append(val)
        for bucket in radixArray:
            while len(bucket) > 0:
                val = bucket.pop()
                array.append(val)

        exp *= 10

print("Sorted array:", my_array)
