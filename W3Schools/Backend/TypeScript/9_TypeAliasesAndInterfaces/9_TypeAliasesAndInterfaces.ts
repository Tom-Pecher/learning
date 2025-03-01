
// TypeScript: W3Schools - Main Tutorial
// Section 9: Type Aliases and Interfaces

// TypeScript allows types to be defined separately from the variables that use them. This can be done in two ways.

// Type aliases allow defining types with a custom name (an alias).
// Type aliases can be used for primitives like string or more complex types such as objects and arrays:
type CarYear = number
type CarType = string
type CarModel = string
type Car = {
    year: CarYear,
    type: CarType,
    model: CarModel
}

const carYear: CarYear = 2001
const carType: CarType = "Toyota"
const carModel: CarModel = "Corolla"
const car: Car = {
    year: carYear,
    type: carType,
    model: carModel
}

// Interfaces are similar to type aliases, except they only apply to object types:
interface Rectangle {
    height: number,
    width: number
}

const rectangle: Rectangle = {
    height: 20,
    width: 10
};

// Interfaces can inherit from other interfaces:
interface ColoredRectangle extends Rectangle {
    color: string
}

const coloredRectangle: ColoredRectangle = {
    height: 20,
    width: 10,
    color: "red"
}
