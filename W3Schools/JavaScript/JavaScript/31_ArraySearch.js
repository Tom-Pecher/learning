
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 31: Array Search

const fruits = ["Apple", "Orange", "Apple", "Mango"];

// The indexOf() method searches an array for an element value and returns its position:
fruits.indexOf("Apple");

// The lastIndexOf() method searches an array for an element value and returns its position:
fruits.lastIndexOf("Apple");

// The includes() method checks if an array contains a specified element:
fruits.includes("Apple");

// The find() method returns the value of the first element in an array that passes a test:
const numbers = [4, 9, 16, 25, 29];
let first = numbers.find(myFunction);

function myFunction(value, index, array) {
  return value > 18;
}

// The findIndex() method returns the index of the first element in an array that passes a test:
numbers.findIndex(myFunction);

// The findLast() method returns the value of the last element in an array that passes a test:
numbers.findLast(myFunction);

// The findLastIndex() method returns the index of the last element in an array that passes a test:
numbers.findLastIndex(myFunction);
