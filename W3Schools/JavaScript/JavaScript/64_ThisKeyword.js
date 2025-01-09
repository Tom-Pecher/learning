
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 64: This Keyword

const person = {
  firstName: "John",
  lastName : "Doe",
  id       : 5566,
  fullName : function() {
    return this.firstName + " " + this.lastName;
  }
};

// The this keyword refers to different objects depending on how it is used:
  // In an object method, this refers to the object.
  // Alone, this refers to the global object.
  // In a function, this refers to the global object.
  // In a function, in strict mode, this is undefined.
  // In an event, this refers to the element that received the event.
  // Methods like call(), apply(), and bind() can refer this to any object.
function myFunction() {
  return this;
}
