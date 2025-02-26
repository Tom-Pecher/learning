
// C#: W3Schools - Main Tutorial
// Section 8: Type Casting

// Type casting is when you assign a value of one data type to another type.
// In C#, there are two types of casting:
//     Implicit Casting (automatically) - converting a smaller type to a larger type size
//          char -> int -> long -> float -> double
//     Explicit Casting (manually) - converting a larger type to a smaller size type
//          double -> float -> long -> int -> char

// Implicit Casting:
int myInt1 = 9;
double myDouble1 = myInt1;

Console.WriteLine(myInt1);
Console.WriteLine(myDouble1);

// Explicit Casting:
double myDouble2 = 9.78;
int myInt2 = (int) myDouble2;

Console.WriteLine(myDouble2);
Console.WriteLine(myInt2);

// Type Conversion Methods:
int myInt = 10;
double myDouble = 5.25;
bool myBool = true;

Console.WriteLine(Convert.ToString(myInt));
Console.WriteLine(Convert.ToDouble(myInt));
Console.WriteLine(Convert.ToInt32(myDouble));
Console.WriteLine(Convert.ToString(myBool));
