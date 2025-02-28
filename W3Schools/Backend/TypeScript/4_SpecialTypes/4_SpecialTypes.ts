
// TypeScript: W3Schools - Main Tutorial
// Section 4: Special Types

// The any data type is the super type of all types in TypeScript:
let v: any = true;
v = "string";
Math.round(v);

// The unknown data type is the type-safe counterpart of any. It is a type that is not known until runtime:
let w: unknown = 1;
w = "string"; // no error
w = {
  runANonExistentMethod: () => {
    console.log("I think therefore I am");
  }
} as { runANonExistentMethod: () => void}

// Error: Object is of type 'unknown'.
// if(typeof w === 'object' && w !== null) {
//   (w as { runANonExistentMethod: Function }).runANonExistentMethod();
// }

// Never is a data type that represents the type of values that never occur (always throws an error):
// let x: never = true;

// Undefined and null refer to the JavaScript undefined and null values:
let y: undefined = undefined;
let z: null = null;
