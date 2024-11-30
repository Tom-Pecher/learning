
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 9: Const

// Consts cannot be reassigned:
const PI = 3.141592653589793;

// Consts must be assigned a value when declared.

// The keyword const is a little misleading.
// It does not define a constant value. It defines a constant reference to a value.
// Because of this you can NOT:
//     Reassign a constant value
//     Reassign a constant array
//     Reassign a constant object

// But you CAN:
//     Change the elements of constant array
//     Change the properties of constant object

//          Scope	Redeclare	Reassign	Hoisted	    Binds this
// var	    No      Yes	        Yes	        Yes	        Yes
// let	    Yes     No	        Yes	        No	        No
// const	Yes     No	        No	        No	        No