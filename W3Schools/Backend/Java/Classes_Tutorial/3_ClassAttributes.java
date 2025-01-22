
// Java: W3Schools - Classes Tutorial
// Section 3: Class Attributes

public class Main {
  int x = 5;  // We can assign attributes to classes.

  public static void main(String[] args) {
    Main myObj1 = new Main();
    Main myObj2 = new Main();
    myObj2.x = 25;    // We can assign and modify attributes.
    System.out.println(myObj1.x);  // The attribute for each object can be different.
    System.out.println(myObj2.x);
  }
}
