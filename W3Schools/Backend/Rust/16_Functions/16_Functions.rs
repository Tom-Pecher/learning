
// Rust: W3Schools - Main Tutorial
// Section 16: Functions

fn main() {
    
    // Functions in Rust are defined using the fn keyword:
    fn add(a: i32, b: i32) -> i32 {
        let c = a + b;

        // Whilst Rust has a return keyword, we can simply return the value directly (without semicolon):
        c
    }
    
    let sum = add(3, 4);
    println!("Sum is: {}", sum);
    
}
