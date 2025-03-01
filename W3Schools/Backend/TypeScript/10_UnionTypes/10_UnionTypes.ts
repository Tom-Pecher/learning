
// TypeScript: W3Schools - Main Tutorial
// Section 10: Union Types

// Union types are used when a value can be more than a single type.
// Using the | we are saying our parameter is a string or number:
function printStatusCode1(code: string | number) {
    console.log(`My status code is ${code}.`)
}
printStatusCode1(404);
printStatusCode1('404');

// NOTE: This can result in errors if the functionality does not support all of the types in the union:
// function printStatusCode2(code: string | number) {
//     console.log(`My status code is ${code.toUpperCase()}.`)
// }
