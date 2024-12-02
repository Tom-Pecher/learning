
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 17: Object Methods


// Here is an example of a method in an object:
const person = {
    firstName: "John",
    lastName: "Doe",
    id: 5566,
    fullName: function() {
        return this.firstName + " " + this.lastName;
    }
};

// We can call it like so:
//      objectName.methodName()

// If we call the property with (), it will execute as a function:
const name1 = person.fullName();

// If we call the property without (), it will return the function definition:
const name2 = person.fullName;

// We can again add methods to an object as we do with properties:
person.name = function () {
    return this.firstName + " " + this.lastName;
};
