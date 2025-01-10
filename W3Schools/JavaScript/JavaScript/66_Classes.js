
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 66: Classes

// Define a class:
class Car {
    // Constructor method:
    constructor(name, year) {
        this.name = name;
        this.year = year;
    }
    // Class methods use the same syntax as object methods:
    age(x) {
        return x - this.year;
    }
}

// Create objects as instances of class:
const myCar1 = new Car("Ford", 2014);
const myCar2 = new Car("Audi", 2019);
