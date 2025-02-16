
# DSA: W3Schools - Arrays Tutorial
# Section 1: Arrays

# An array is a data structure used to store multiple elements:
my_array = [7, 12, 9, 4, 11]

# Arrays are indexed, meaning that each element in the array has an index, a number that says where in the array the element is located:
minVal = my_array[0]

# Loop through the array and find the lowest value:
for i in my_array:
    if i < minVal:
        minVal = i
        
print('Lowest value: ',minVal)

# This method has a time complexity of O(n) because it loops through each element in the array.
