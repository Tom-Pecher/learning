// TypeScript: W3Schools - Main Tutorial
// Section 12: Casting
// A straightforward way to cast a variable is using the as keyword, which will directly change the type of the given variable:
var x1 = 'hello';
console.log(x1.length);
// Another way to cast a variable is using the <> syntax (these are effectively the same):
var x2 = 'hello';
console.log(x2.length);
// To override type errors that TypeScript may throw when casting, first cast to unknown, then to the target type. 
// This is called a double assertion (or forced casting):
// let x3 = 'hello';
// console.log(((x3 as unknown) as number).length); // x is not actually a number so this will return undefined 
