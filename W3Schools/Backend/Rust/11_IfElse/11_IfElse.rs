
// Rust: W3Schools - Main Tutorial
// Section 11: If/Else

fn main() {
    let x = 7;
    let y = 5;

    // We can make conditional statements using boolean expressions:
    if x > y {
        println!("x is greater than y.");
    } else if x < y {
        println!("x is less than y.");
    } else {
        println!("x is equal to y.");
    }

    // We can also use if as an expression:
    let time = 20;
    let greeting = if time < 18 {
        "Good day."
    } else {
        "Good evening."
    };
    println!("{}", greeting);
}
