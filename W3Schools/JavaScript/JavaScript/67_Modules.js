
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 67: Modules

// It is often useful to divide up one's code into separate modules.
// This can be done by creating separate files for each module and importing them into the main file:
import message from "./message.js";

// Likewise, we can also export variables from a module:
const name = "Jesse";
const age = 40;

export {name, age};
