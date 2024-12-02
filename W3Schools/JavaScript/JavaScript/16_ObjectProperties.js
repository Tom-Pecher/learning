
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 16: Object Properties


// Properties were covered in the last topic.
// To delete a property, use the delete keyword:
const person = {
    firstName: "John",
    lastName: "Doe",
    age: 50,
    eyeColor: "blue"
  };

delete person.age;
delete person["eyeColor"];

// We can also nest objects and hence properties inside one another:
myObj = {
    name:"John",
    age:30,
    myCars: {
        car1:"Ford",
        car2:"BMW",
        car3:"Fiat"
    }
}
