
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 53: Maps

// Maps allow us to save key-value pairs in a collection:
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);

// Add a new key-value pair to the map:
fruits.set("pears", 700);

// Return the value corresponding to a key:
fruits.get("apples");

// The instanceof returns true for Map:
fruits instanceof Map;
