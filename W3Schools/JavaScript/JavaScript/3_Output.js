
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 3: Output

// JavaScript can "display" data in different ways.


//// Using innerHTML
// To access an HTML element, JavaScript can use the document.getElementById(id) method.
// The id attribute defines the HTML element. The innerHTML property defines the HTML content:
/* 
<p id="demo"></p>

<script>
document.getElementById("demo").innerHTML = 5 + 6;
</script>
*/


//// Using document.write()
// For testing purposes, it is convenient to use document.write():
/* 
<script>
document.write(5 + 6);
</script> 
*/

// Using document.write() after an HTML document is loaded, will delete all existing HTML:
// Hence, the document.write() method should only be used for testing.


//// Using window.alert()
// You can use an alert box to display data:
/*
<script>
window.alert(5 + 6);
</script>
*/

// In JavaScript, the window object is the global scope object. 
// This means that variables, properties, and methods by default belong to the window object. 
// This also means that specifying the window keyword is optional.


//// Using console.log()
// For debugging purposes, you can use the console.log() method:
console.log(5 + 6);

// The console.log() method writes a message to the console.


//// JavaScript Print:
// JavaScript does not have a print function.
// You cannot access output devices from JavaScript.
// The only exception is that you can call the window.print() method in the browser to print the content of the current window.
/* 
<button onclick="window.print()">Print this page</button>
*/
