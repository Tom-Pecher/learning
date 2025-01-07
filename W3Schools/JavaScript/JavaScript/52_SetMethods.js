
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 52: Set Methods


const letters = new Set(["a","b","c"]);

// Add a new value to the set:
letters.add("d");

// The has() method returns true if a value exists in the set:
letters.has("d");

// The forEach() method calls a function once for each value in the set:
let text = "";
letters.forEach (function(value) {
  text += value;
})

// The values() method returns an iterator object with the values of the set:
for (const entry of letters.values()) {
  text += entry;
}

// The keys() method returns an iterator object with the keys of the set:
for (const entry of letters.keys()) {
  text += entry;
}

// The entries() method returns an iterator object with the key/value pairs of the set:
for (const entry of letters.entries()) {
  text += entry;
}
