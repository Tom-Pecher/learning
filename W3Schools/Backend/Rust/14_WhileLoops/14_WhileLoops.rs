
// Rust: W3Schools - Main Tutorial
// Section 14: While Loops

fn main() {
    
    let mut num = 1;

    // While loops (like in most other languages), run until their condition is false:
    while num <= 10 {

        // The continue keyword skips the current iteration:
        if num == 4 {
            num += 1;
            continue;
        }

        // The break keyword stops the loop:
        if num == 8 {
            break;
        }

        println!("Number: {}", num);
        num += 1;

    } 
}
