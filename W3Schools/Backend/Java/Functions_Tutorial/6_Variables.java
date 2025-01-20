
// Java: W3Schools - Functions Tutorial
// Section 1: Methods

// Methods are blocks of code that can be run when called.

public class Main {
  // Methods must be defined within a class.

  // We can define a method using the following syntax:
  static void myMethod() {  // static means that the method belongs to the Main class and not an object of the Main class.
    System.out.println("I just got executed!");
  }

  // The main method is the entry point of a Java program:
  public static void main(String[] args) {
    myMethod();
  }
}