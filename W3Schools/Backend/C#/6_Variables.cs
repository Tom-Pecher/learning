
// C#: W3Schools - Main Tutorial
// Section 6: Variables

// Variables in C# work the same as in any other programming language:
string name = "John";
Console.WriteLine(name);

// Some basic types include:
int myNum1 = 5;
double myDoubleNum = 5.99D;
char myLetter = 'D';
bool myBool = true;
string myText = "Hello";

// A constant is a variable whose value cannot change once it has been assigned:
const int myNum2 = 15;

// NOTE: That constants must be declared with a value.

// Multiple variables can be declared in one line:
int x1 = 5, y1 = 6, z1 = 50;
Console.WriteLine(x1 + y1 + z1);

// Multiple variables can be given the same value:
int x2, y2, z2;    // Declare variables
x2 = y2 = z2 = 50; // Assign the same value to all three variables
Console.WriteLine(x2 + y2 + z2);
