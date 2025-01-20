
// Java: W3Schools - Functions Tutorial
// Section 5: Recursion

public class Main {

  public static void main(String[] args) {
    int result = sum(10);
    System.out.println(result);
  }

  // A function can call itself. This is known as recursion:
  public static int sum(int k) {
    if (k > 0) {
      return k + sum(k - 1);
    } else {
      return 0;
    }
  }
}
