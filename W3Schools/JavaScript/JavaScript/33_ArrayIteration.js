
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 33: Array Iteration

const numbers = [45, 4, 9, 16, 25];
function myFunction(value, index, array) {
    return value * 2;
  }

// The forEach() method calls a function (a callback function) once for each array element:
numbers.forEach(myFunction);

// The map() method creates a new array by performing a function on each array element:
numbers.map(myFunction);

// The flatMap() method creates a new array by performing a function on each array element, and then flattening the result into a new array:
myArr.flatMap((x) => x * 2);

// The filter() method creates a new array with array elements that passes a test:
numbers.filter(myFunction);

// The reduce() method runs a function on each array element to produce (reduce it to) a single value:
numbers.reduce(myFunction);

// The reduceRight() method runs a function on each array element to produce (reduce it to) a single value from right to left:
numbers.reduceRight(myFunction);

// The every() method checks if all array values pass a test:
numbers.every(myFunction);

// The some() method checks if some array values pass a test:
numbers.some(myFunction);

// The from() method creates an Array object from any object with a length property or an iterable object:
Array.from("ABCDEFG");

// The keys() method returns an Array Iteration Object, containing the keys of the original array:
const fruits = ["Banana", "Orange", "Apple", "Mango"];
const keys = fruits.keys();

// The entries() method returns an Array Iteration Object, containing the values of the original array:
fruits.entries();

// The with() method returns an Array Iteration Object, containing the key/value pairs of the original array:
fruits.with(2, "Kiwi");

// The spread operator can be used to merge two arrays:
newArr = [...numbers, ...fruits];
