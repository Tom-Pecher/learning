
// C#: W3Schools - Main Tutorial
// Section 15: Switch

// A switch statement allows a variable to be tested for equality against a list of values:
int day = 4;
switch (day) 
{
  case 6:
    Console.WriteLine("Today is Saturday.");
    break;  // break is used to exit the switch statement
  case 7:
    Console.WriteLine("Today is Sunday.");
    break;
  default:  // default is used when no case matches
    Console.WriteLine("Looking forward to the Weekend.");
    break;
}
