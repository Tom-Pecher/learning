
// Rust: W3Schools - Main Tutorial
// Section 6: Variables

fn main() {
    // Variables are containers for storing data values:
    let firstname = "John";
    println!("My first name is: {}", firstname);

    // The {} is a placeholder for a variable, placeholders are filled in order:
    println!("My name is {} {}", firstname, "Doe");

    // Or we can set the order:
    println!("My name is {1} {0}", firstname, "Doe");

    // In Rust, all variables are constant by default and must be explicitly marked as mutable:
    let mut x = 5;
    println!("Before: {}", x);
    x = 10;
    println!("After: {}", x); 
}
