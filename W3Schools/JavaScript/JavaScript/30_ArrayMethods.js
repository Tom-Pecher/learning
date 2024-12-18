
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 30: Array Methods

const fruits = ["Banana", "Orange", "Apple", "Mango"];

// Get array length:
fruits.length;

// Convert to string:
document.getElementById("demo").innerHTML = fruits.toString();

// Obtain element at index:
fruits.at(2);

// Join list together:
fruits.join(" * ");

// Remove and return last element:
fruits.pop();

// Add element to end:
fruits.push("Kiwi");

// Remove and return first element, shifting all other elements down:
fruits.shift();

// Add element to start:
fruits.unshift("Lemon");

// Delete element, leaves undefined:
delete fruits[0];

// Concatenate two arrays:
const vegetables = ["Potato", "Tomato"];
vegetables.concat(myBoys);

// The copyWithin() method copies array elements to another position in an array:
fruits.copyWithin(2, 0);

// Flatten an array:
const myArr = [[1,2],[3,4],[5,6]];
myArr.flat();

// Add elements to array (where they should be added, and how many to remove):
fruits.splice(2, 0, "Lemon", "Kiwi");

// Create a spliced array whilst keeping the original:
const months = ["Jan", "Feb", "Mar", "Apr"];
months.toSpliced(0, 1);

// Get a slice of an array:
fruits.slice(1, 3);
