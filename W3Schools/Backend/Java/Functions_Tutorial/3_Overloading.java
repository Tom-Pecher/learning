
// Java: W3Schools - Functions Tutorial
// Section 3: Overloading


public class Main {
  // We can overload a method to work for different parameter types:
  static int plusMethod(int x, int y) {
    return x + y;
  }

  // We do this by redefining the method with the same name:
  static double plusMethod(double x, double y) {
    return x + y;
  }

  public static void main(String[] args) {
    int myNum1 = plusMethod(8, 5);
    double myNum2 = plusMethod(4.3, 6.26);
    System.out.println("int: " + myNum1);
    System.out.println("double: " + myNum2);
  }
}
