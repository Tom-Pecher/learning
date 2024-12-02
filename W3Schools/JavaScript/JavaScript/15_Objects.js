
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 15: Objects


// JavaScript objects are containers for properties or methods:
const car = {type:"Fiat", model:"500", color:"white"};

// It is good practice to declare objects with the const keyword.
// We can have object literals too.

// We can add properties to an object by simply giving them a value:
const person1 = {};
person1.firstName = "John";
person1.lastName = "Doe";
person1.age = 50;
person1.eyeColor = "blue";

// Create object using new keyword:
const person1 = new Object();

// We can access object properties in two ways:
//      1. objectName.propertyName
//      2. objectName["propertyName"]

// Objects can also have methods:
const person2 = {
    firstName: "John",
    lastName : "Doe",
    id       : 5566,
    fullName : function() {
        return this.firstName + " " + this.lastName;  // 'this' keyword refers to the instance
    }
};

// JavaSript defines the following primitives:
//     - string
//     - number
//     - boolean
//     - null
//     - undefined
//     - symbol
//     - bigint

// Primitive values are immutable but objects are mutable.