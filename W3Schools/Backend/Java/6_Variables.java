
// Java: W3Schools - Main Tutorial
// Section 6: Variables

// Java Variable Types:
//      - String
//      - int
//      - float
//      - boolean
//      - char

public class Main {
  public static void main(String[] args) {

    int myNum1;    // Declare a variable
    myNum1 = 15;   // Assign a value

    // Print the value of the variable:
    System.out.println(myNum1);

    // Final variables cannot be changed once they are assigned a value:
    final int myNum2 = 15;
    
    // Example of all variable types:
    int myNum = 5;
    float myFloatNum = 5.99f;
    char myLetter = 'D';
    boolean myBool = true;
    String myText = "Hello";

    // We can also declare multiple variables in one line:
    int x1 = 5, y1 = 6, z1 = 50;
    System.out.println(x1 + y1 + z1);

    // Or declare multiple variables with the same value:
    int x2, y2, z2;
    x2 = y2 = z2 = 50;
    System.out.println(x2 + y2 + z2);

  }
}
