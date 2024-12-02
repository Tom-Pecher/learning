
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 18: Object Display


const person = {
    name: "John",
    age: 30,
    city: "New York"
};
  
// Display the object in HTML (as a string):
document.getElementById("demo").innerHTML = person;

// We can also use a loop to build the text of the property values:
let text1 = "";
for (let x in person) {
  text1 += person[x] + " ";
};
document.getElementById("demo").innerHTML = text1;

// We can also use the Object.entries() method to get an array of the object's properties:
const fruits = {Bananas:300, Oranges:200, Apples:500};
let text2 = "";
for (let [fruit, value] of Object.entries(fruits)) {
  text2 += fruit + ": " + value + "<br>";
}

// We can also use the Object.values() method to get an array of the object's values:
const myArray = Object.values(person);
document.getElementById("demo").innerHTML = myArray;

// We can also use the JSON.stringify() method to convert the object into a string:
const myString = JSON.stringify(person);
document.getElementById("demo").innerHTML = myString;
