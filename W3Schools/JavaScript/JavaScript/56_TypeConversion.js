
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 55: Type Conversion

// The global method Number() converts a variable (or a value) into a number.
Number("3.14")
Number(Math.PI)
Number(" ")
Number("")

// The global method String() can convert a number to a string.
String(123)
String(100 + 23)
String(100 + "23")

// The global method Boolean() can convert a value to a boolean.
Boolean(0)
Boolean(1)
Boolean("Hello")

// JavaScript Conversion Table:
//    VALUE: 	        NUMBER: 	    STRING: 	        BOOLEAN:
//    false 	        0 	            "false" 	        false 	
//    true 	            1 	            "true" 	            true 	
//    0 	            0 	            "0" 	            false 	
//    1 	            1 	            "1" 	            true 	
//    "0" 	            0 	            "0" 	            true 	
//    "000" 	        0 	            "000" 	            true 	
//    "1" 	            1 	            "1" 	            true 	
//    NaN 	            NaN 	        "NaN" 	            false 	
//    Infinity 	        Infinity 	    "Infinity" 	        true 	
//    -Infinity 	    -Infinity 	    "-Infinity" 	    true 	
//    "" 	            0 	            "" 	                false 	
//    "20" 	            20 	            "20" 	            true 	
//    "twenty" 	        NaN 	        "twenty" 	        true 	
//    [ ] 	            0 	            "" 	                true 	
//    [20] 	            20 	"           20" 	            true 	
//    [10,20] 	        NaN 	        "10,20" 	        true 	
//    ["twenty"] 	    NaN 	        "twenty" 	        true 	
//    ["ten","twenty"] 	NaN 	        "ten,twenty" 	    true 	
//    function(){} 	    NaN 	        "function(){}" 	    true 	
//    { } 	            NaN 	        "[object Object]" 	true 	
//    null 	            0 	            "null" 	            false 	
//    undefined 	    NaN 	        "undefined" 	    false
