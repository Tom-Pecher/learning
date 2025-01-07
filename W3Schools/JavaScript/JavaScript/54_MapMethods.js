
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 54: Map Methods

const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);

// Get value of key:
fruits.get("apples");

// Add a new key-value pair to the map:
fruits.set("pears", 700);

// Obtain the size of the map:
fruits.size;

// Delete a key-value pair:
fruits.delete("apples");

// Remove all key-value pairs:
fruits.clear();

// Return true if a specified key exists in the map:
fruits.has("apples");

// Invoke a function for each key-value pair:
let text = "";
fruits.forEach (function(value, key) {
  text += key + ' = ' + value;
})

// Return an iterator of the entries:
for (const x of fruits.entries()) {
  text += x;
}

// Return an iterator of the keys:
for (const x of fruits.keys()) {
  text += x;
}

// Return an iterator of the values:
for (const x of fruits.values()) {
  text += x;
}

// Being able to use objects as keys is an important Map feature;
const apples = {name: 'Apples'};
const bananas = {name: 'Bananas'};
const oranges = {name: 'Oranges'};

const more_fruits = new Map();

more_fruits.set(apples, 500);
more_fruits.set(bananas, 300);
more_fruits.set(oranges, 200);

// Group methods based on string values returned by a callback function:
function myCallback({ quantity }) {
  return quantity > 200 ? "ok" : "low";
}

const result = Map.groupBy(fruits, myCallback);
