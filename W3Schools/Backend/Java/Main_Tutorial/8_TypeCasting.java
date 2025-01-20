
// Java: W3Schools - Main Tutorial
// Section 8: Type Casting

// In Java, there are two types of casting:
    // Widening Casting (automatically), converting a smaller type to a larger type size:
    //  byte -> short -> char -> int -> long -> float -> double

    // Narrowing Casting (manually), converting a larger type to a smaller size type:
    //  double -> float -> long -> int -> char -> short -> byte 

public class Main {
  public static void main(String[] args) {

    // Widening Casting:
    int myInt1 = 9;
    double myDouble1 = myInt1;

    System.out.println(myInt1);
    System.out.println(myDouble1);


    // Narrowing Casting:
    double myDouble2 = 9.78;
    int myInt2 = (int) myDouble2;

    System.out.println(myInt2);
    System.out.println(myDouble2);

  }
}
