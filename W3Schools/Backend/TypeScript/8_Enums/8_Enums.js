// TypeScript: W3Schools - Main Tutorial
// Section 8: Enums
// Enums in TypeScript work the same as in JavaScript (mostly). There are two types of enum.
// Numeric Enums:
var StatusCodes;
(function (StatusCodes) {
    StatusCodes[StatusCodes["NotFound"] = 404] = "NotFound";
    StatusCodes[StatusCodes["Success"] = 200] = "Success";
    StatusCodes[StatusCodes["Accepted"] = 202] = "Accepted";
    StatusCodes[StatusCodes["BadRequest"] = 400] = "BadRequest";
})(StatusCodes || (StatusCodes = {}));
;
console.log(StatusCodes.NotFound);
console.log(StatusCodes.Success);
// String Enums:
var CardinalDirections;
(function (CardinalDirections) {
    CardinalDirections["North"] = "North";
    CardinalDirections["East"] = "East";
    CardinalDirections["South"] = "South";
    CardinalDirections["West"] = "West";
})(CardinalDirections || (CardinalDirections = {}));
;
console.log(CardinalDirections.North);
console.log(CardinalDirections.West);
