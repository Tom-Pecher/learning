
// Rust: W3Schools - Main Tutorial
// Section 13: Loops

fn main() {
    
    // The simplest Rust loop is a loop with no condition, the simplest kind, that repeates forever until broken from within:
    let mut count = 1;

    loop {
        println!("{}. Hello World!", count);

    if count == 3 {
        // Break out of the loop:
        break;
    }
        count += 1;
    } 
}
