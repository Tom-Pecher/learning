
// Rust: W3Schools - Main Tutorial
// Section 12: Match

fn main() {
    let day = 6;
  
    // A match statement allows us to execute different code based on the value of a variable:
    let result = match day {
        1 | 2 | 3 | 4 | 5 => "Weekday",
        6 | 7 => "Weekend",
        _ => "Invalid day",
    };

    println!("{}", result);
}
