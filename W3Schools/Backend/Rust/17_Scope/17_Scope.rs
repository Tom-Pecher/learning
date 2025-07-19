
// Rust: W3Schools - Main Tutorial
// Section 17: Scope

fn main() {

    // Like similarly syntaxed languages, Rust has block scope:
    
    let score = 80;

    if score > 50 {
    let result = "Pass";
    println!("Result: {}", result);
    }

    // Error: `result` does not exist here:
    // println!("Result: {}", result);

}
