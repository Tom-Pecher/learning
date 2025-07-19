
// Rust: W3Schools - Main Tutorial
// Section 15: For Loops

fn main() {
    
    // The for loop allows us to iterate over values of a variable:
    for i in 1..6 {
        println!("i is: {}", i);
    }

    // If we wish to include the last value, we can use the ..= operator:
    for i in 1..=6 {
        println!("i is: {}", i);
    } 
}
