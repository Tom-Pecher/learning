
// Java: W3Schools - Main Tutorial
// Section 17: Continue


public class Main {
  public static void main(String[] args) {

    String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
    for (String i : cars) {

      // The continue statement skips one iteration of a loop.
      if (i == "BMW") {
        continue;
      }
      System.out.println(i);
    }

  }
}
