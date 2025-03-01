
// TypeScript: W3Schools - Main Tutorial
// Section 12: Casting

// A straightforward way to cast a variable is using the as keyword, which will directly change the type of the given variable:
let x1: unknown = 'hello';
console.log((x1 as string).length);

// Another way to cast a variable is using the <> syntax (these are effectively the same):
let x2: unknown = 'hello';
console.log((<string>x2).length);

// To override type errors that TypeScript may throw when casting, first cast to unknown, then to the target type. 
// This is called a double assertion (or forced casting):
// let x3 = 'hello';
// console.log(((x3 as unknown) as number).length); // x is not actually a number so this will return undefined 
