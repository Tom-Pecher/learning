
// Java: W3Schools - Main Tutorial
// Section 10: Strings


public class Main {
  public static void main(String[] args) {

    // Strings:
    String txt = "Hello";

    // String length:
    System.out.println("The length of the txt string is: " + txt.length());

    // Convert between cases:
    System.out.println(txt.toUpperCase());
    System.out.println(txt.toLowerCase());

    // Finding a character in a string:
    System.out.println(txt.indexOf("e"));

    // Concatenation:
    String firstName = "John";
    String lastName = "Doe";
    System.out.println(firstName + " " + lastName);
    System.out.println(firstName.concat(lastName));

    // Numbers will be implicitly converted to strings when operated on by them:
    String x = "10";
    int y = 20;
    String z = x + y;

  }
}

// Escape characters:
  //  \' 	  Single quote
  //  \" 	  Double quote
  //  \\ 	  Backslash
  //  \n 	  New Line 	
  //  \r 	  Carriage Return 	
  //  \t 	  Tab 	
  //  \b 	  Backspace 	
  //  \f 	  Form Feed
  