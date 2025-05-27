
// Rust: W3Schools - Main Tutorial
// Section 10: Booleans

fn main() {
    // Booleans are used for storing true/false values:
    let is_programming_fun: bool = true;
    let is_fish_tasty: bool = false;

    // Comparison operators return booleans:
    println!("{}", is_programming_fun && is_fish_tasty);

    // We can use conditional statements using boolean expressions:
    if is_programming_fun {
        println!("Programming is fun!");
    } else {
        println!("Programming is not fun?");
    }
}
