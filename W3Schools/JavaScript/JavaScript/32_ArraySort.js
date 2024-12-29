
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 32: Array Sort

const fruits = ["Banana", "Orange", "Apple", "Mango"];

// The sort() method sorts an array alphabetically:
fruits.sort();

// We can modify the sort order by passing a compare function:
const points = [40, 100, 1, 5, 25, 10];
points.sort(function(a, b){return a - b});

// The reverse() method reverses the elements in an array:
fruits.reverse();

// The toSorted() method sorts an array without altering the original:
fruits.toSorted();

// The toReversed() method reverses the elements in an array without altering the original:
fruits.toReversed();
