
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 68: JSON

// JSON is a format for storing and transporting data:
// {
//     "employees":[
//       {"firstName":"John", "lastName":"Doe"},
//       {"firstName":"Anna", "lastName":"Smith"},
//       {"firstName":"Peter", "lastName":"Jones"}
//     ]
// }

// JSON data is written as name/value pairs.
// JSON arrays are written inside square brackets.
// JSON objects are written inside curly brackets.

// Here is how we convert for a JSON string to a JavaScript object:
let text = '{ "employees" : [' +
'{ "firstName":"John" , "lastName":"Doe" },' +
'{ "firstName":"Anna" , "lastName":"Smith" },' +
'{ "firstName":"Peter" , "lastName":"Jones" } ]}'; 
const obj = JSON.parse(text);
