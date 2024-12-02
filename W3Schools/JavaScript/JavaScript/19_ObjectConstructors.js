
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 19: Object Constructors


// Instead of objects being simple contariners of key-value pairs, we can use them to create custom data types.
// To do this, we must create a constructor function:
function Person(first, last, age, eye) {
    this.firstName = first;
    this.lastName = last;
    this.age = age;
    this.eyeColor = eye;
    this.nationality = "English"; // We can give default values to properties
}

// Now we can create person objects using the constructor function:
const myFather = new Person("John", "Doe", 50, "blue");
const myMother = new Person("Sally", "Rally", 48, "green");
const mySister = new Person("Anna", "Rally", 18, "green");

// Now, we can not longer add properties to the object constructor, but we can add properties to the constructor function using the prototype property:
Person.prototype.nationality = "English";

// We can also add methods to the constructor function:
Person.prototype.changeName = function (name) {
  this.lastName = name;
}

// Here are the built-in object constructors:
new Object()   // A new Object object
new Array()    // A new Array object
new Map()      // A new Map object
new Set()      // A new Set object
new Date()     // A new Date object
new RegExp()   // A new RegExp object
new Function() // A new Function object

// It is better to use object literals to create builtin objects:
"";                 // primitive string
0;                  // primitive number
false;              // primitive boolean

{};                 // object object
[];                 // array object
/()/                // regexp object
function test(){};  // function 
