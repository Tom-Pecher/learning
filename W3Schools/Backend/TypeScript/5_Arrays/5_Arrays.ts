
// TypeScript: W3Schools - Main Tutorial
// Section 5: Arrays

// TypeScript has a specific syntax for arrays. It is similar to JavaScript, but with a few differences:
const names1: string[] = [];
names1.push("Dylan");

// The readonly keyword is used to make the array immutable. This means that you cannot add, remove, or change elements in the array:
const names2: readonly string[] = ["Dylan"];

// NOTE: TypeScript will infer the type of the array if you initialize it with values.
