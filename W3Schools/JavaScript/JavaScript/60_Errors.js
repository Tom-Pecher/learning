
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 60: Errors

// The try statement lets you test a block of code for errors:
try {
    // Block of code to try
}
catch(err) {
    // Block of code to handle errors
}
finally {
    // Block of code to be executed regardless of the try/catch result
} 

// The throw statement lets you create custom errors:
throw "Too big";

// Erros have two properties:
    // name	    Sets or returns an error name
    // message	Sets or returns an error message (a string)

// Some common errors include:
    // EvalError	    An error has occurred in the eval() function
    // RangeError	    A number "out of range" has occurred
    // ReferenceError	An illegal reference has occurred
    // SyntaxError	    A syntax error has occurred
    // TypeError	    A type error has occurred
    // URIError	        An error in encodeURI() has occurred
    