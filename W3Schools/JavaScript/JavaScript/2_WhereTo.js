
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 2: Where To

// In HTML, JavaScript code is inserted between <script> and </script> tags.
// A JavaScript function is a block of JavaScript code, that can be executed when "called" for.
// Scripts can also be placed in external files:
function myFunction() {
    document.getElementById("demo").innerHTML = "Paragraph changed.";
}

// To use an external script, put the name of the script file in the src (source) attribute of a <script> tag:
// <script src="myScript.js"></script>

// We can reference an external script in 3 ways:
//   - With a full URL (a full web address):        <script src="https://www.w3schools.com/js/myScript.js"></script> 
//   - With a file path (like /js/):                <script src="/js/myScript.js"></script> 
//   - Without any path                             <script src="myScript.js"></script> 
