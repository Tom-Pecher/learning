
// RUST: Rust By Example
// Section 1.6: Display

// Import format module:
use std::fmt;

// Define a structure named `List` containing a `Vec`.
struct List(Vec<i32>);

impl fmt::Display for List {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // Create reference to the vector inside the List:
        let vec = &self.0;

        // Try `write!` to see if it errors. If it errors, return
        // the error. Otherwise continue.
        write!(f, "[")?;

        // Iterate over `vec`, printing each element:
        for (count, v) in vec.iter().enumerate() {
            // For every element except the first, add a comma.
            // Use the ? operator to return on errors.
            if count != 0 { write!(f, ", ")?; }

            // Activity 1:
            write!(f, "{}: {}", count, v)?;
        }

        // Close the opened bracket and return a fmt::Result value.
        write!(f, "]")
    }
}

fn main() {
    let v = List(vec![1, 2, 3]);
    println!("{}", v);
}
