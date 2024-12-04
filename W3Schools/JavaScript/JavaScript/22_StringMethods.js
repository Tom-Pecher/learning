
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 22: String Methods

let text = "HELLO WORLD";

// Since strings are primitives and immutable, string methods only create new strings:

// Return character at index:
text.charAt(0);

// Return the UTF-16 code of character at index:
text.charCodeAt(0);

// Return character at index (allows negatives)
text.at(0);
text[0];

// Extract part of a string:
text.slice(1, 4);       // extract from a to b (includes negatives)
text.substring(1, 4);   // extract from a to b (negatives set to 0)
text.subst(1, 3);       // extract from a to a+b

// Convert to uppercase
text.toUpperCase();      

// Convert to lowercase
text.toLowerCase();

// Concatenate strings
text.concat(" ", "WORLD");
text + " more";

// Remove whitespaces from ends of string
text.trim();
text.trimStart();   // remove whitespaces from start only
text.trimEnd();     // remove whitespaces from end only

// Pad a string with a specified other string:
text.padStart(20, "*");
text.padEnd(20, "*");

// Repeat string a specified number of times:
text.repeat(2);

// Replace a substring with another substring:
text.replace("WORLD", "MARS");
text.replaceAll("L", "X");

// Split a string based on specific characters:
text.split(" ");
