
// Java: W3Schools - Main Tutorial
// Section 13: If Else


public class Main {
  public static void main(String[] args) {

    int time = 22;

    // We can use if-else statements to make decisions based on conditions
    if (time < 10) {
      System.out.println("Good morning.");
    } else if (time < 18) {
      System.out.println("Good day.");
    } else {
      System.out.println("Good evening.");
    }

    // We can also write this in shorthand using a ternary operator:
    String result = (time < 18) ? "Good day." : "Good evening.";
    System.out.println(result);

  }
}
