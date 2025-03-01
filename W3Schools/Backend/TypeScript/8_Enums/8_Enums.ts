
// TypeScript: W3Schools - Main Tutorial
// Section 8: Enums

// Enums in TypeScript work the same as in JavaScript (mostly). There are two types of enum.
// Numeric Enums:
enum StatusCodes {
    NotFound = 404,
    Success = 200,
    Accepted = 202,
    BadRequest = 400
};
console.log(StatusCodes.NotFound);
console.log(StatusCodes.Success);

// String Enums:
enum CardinalDirections {
    North = "North",
    East = "East",
    South = "South",
    West = "West"
};
console.log(CardinalDirections.North);
console.log(CardinalDirections.West);
