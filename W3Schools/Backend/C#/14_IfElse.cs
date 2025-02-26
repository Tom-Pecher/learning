
// C#: W3Schools - Main Tutorial
// Section 14: If Else

// The if-else (typical of most languages) statements allow us to execute different code based on boolean conditions:
int time = 22;
if (time < 10) 
{
  Console.WriteLine("Good morning.");
} 
else if (time < 20) 
{
  Console.WriteLine("Good day.");
} 
else 
{
  Console.WriteLine("Good evening.");
}

// We can write this in shorthand using a ternary operator:
string result = (time < 18) ? "Good day." : "Good evening.";
Console.WriteLine(result);
