
// Java: W3Schools - Functions Tutorial
// Section 2: Parameters


public class Main {
  // We can set methods to take values as input parameters:
  static void myMethod1(String fname, int age) {
    System.out.println(fname + " is " + age);
  }

  // Likewise we can set methods to return values:
  static int myMethod2(int x) {
    return 5 + x;
  }

  public static void main(String[] args) {
    myMethod("Liam", 5);
    myMethod("Jenny", 8);

    System.out.println(myMethod(31));
  }
}