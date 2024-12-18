
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 29: Arrays

// An array is a special variable, which can hold more than one value:
const cars = [
    "Saab",
    "Volvo",
    "BMW"
];

// In JavaScript, arrays use numbered indexes.  
// In JavaScript, objects use named indexes.

// You access an array element by referring to the index number:
let car1 = cars[0];
cars[0] = "Opel";

// Converting an array to a string will result in a comma separated string:
document.getElementById("demo").innerHTML = cars.toString();

// Get array length:
cars.length

// Get last element
let car2 = cars[cars.length - 1];

// Sort an array:
cars.sort();

// Looping through an array using forEach:
const fruits = ["Banana", "Orange", "Apple", "Mango"];

let text = "<ul>";
fruits.forEach(myFunction);
text += "</ul>";

function myFunction(value) {
  text += "<li>" + value + "</li>";
}

// Adding array elements:
fruits.push("Lemon");

// Create an array with n undefined elements:
const points = new Array(40);

// Check if variable is an array:
Array.isArray(fruits);
