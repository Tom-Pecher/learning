
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 50: Iterables


// Iterables can be iterated over with for...of loops:
function myNumbers() {
  let n = 0;
  return {
    next: function() {
      n += 10;
      return {value:n, done:false};
    }
  };
}

// Create Iterable
const n = myNumbers();
n.next();
n.next();
n.next();
