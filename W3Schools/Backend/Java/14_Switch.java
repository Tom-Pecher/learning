
// Java: W3Schools - Main Tutorial
// Section 14: Switch


public class Main {
  public static void main(String[] args) {

    int day = 4;

    // We can use switch statements to select one of many code blocks to be executed:
    switch (day) {
      case 6:
        System.out.println("Today is Saturday");
        break;  // The break keyword is used to halt execution of the switch statement.
      case 7:
        System.out.println("Today is Sunday");
        break;
      default:  // The default keyword specifies some code to run if there is no case match.
        System.out.println("Looking forward to the Weekend");
    }

  }
}
