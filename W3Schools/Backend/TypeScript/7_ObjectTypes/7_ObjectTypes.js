// TypeScript: W3Schools - Main Tutorial
// Section 7: Object Types
// TypeScript has a specific syntax for object types. It is similar to JavaScript, but with a few differences:
var car1 = {
    type: "Toyota",
    model: "Corolla",
    year: 2009
};
// NOTE: TypeScript can infer the types of properties based on their values.
// We can add optional properties to an object type by using the ? symbol:
var car2 = {
    type: "Toyota"
};
car2.mileage = 2000;
// Index signatures allow us an additional set of properties with a specific type:
var nameAgeMap = {};
nameAgeMap.Jack = 25;
nameAgeMap.Jill = 23;
