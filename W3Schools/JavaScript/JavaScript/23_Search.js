
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 23: String Search


let text = "Please locate where 'locate' occurs!";

// Return index of first occurrence of a specified substring in a string:
text.indexOf("locate");

// Return index of last occurrence of a specified substring in a string:
text.lastIndexOf("locate");

// Return index of first occurrence of a specified substring/regex in a string:
text.search("locate");

// Return an array of result from matching string against another string/regex:
text.match(/ain/g);

// Return boolean of whether a string contains a specified substring:
text.includes("world");

// Return boolean of whether a string starts with a specified substring:
text.startsWith("Hello");

// Return boolean of whether a string ends with a specified substring:
text.endsWith("world!");
