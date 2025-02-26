
// C#: W3Schools - Main Tutorial
// Section 12: Strings

// Strings are used for storing text:
string greeting = "Hello";

// Get a string's length using the Length attribute:
Console.WriteLine("The length of the txt string is: " + greeting.Length);

// Convert a string to uppercase using ToUpper():
Console.WriteLine(greeting.ToUpper());

// Convert a string to lowercase using ToLower():
Console.WriteLine(greeting.ToLower());

string firstName = "John ";
string lastName = "Doe";

// Concatenate two strings using the + operator:
Console.WriteLine(firstName + lastName);

// Alternatively, use the Concat() method:
Console.WriteLine(string.Concat(firstName, lastName));

// For more detailed string formatting, we can use string interpolation ($):
string name = $"My full name is: {firstName} {lastName}";
Console.WriteLine(name);

// We can index strings like arrays:
string myString = "Hello";
Console.WriteLine(myString[1]);

// Find the index of the first occurrence of a character in a string using IndexOf():
Console.WriteLine(myString.IndexOf("e"));

// Extract a substring using Substring():
Console.WriteLine(myString.Substring(1, 3));


// SPECIAL CHARACTERS
    //  \' 	    ' 	Single quote
    //  \" 	    " 	Double quote
    //  \\ 	    \ 	Backslash
    //  \n 	        New Line 	
    //  \t 	        Tab 	
    //  \b 	        Backspace
    