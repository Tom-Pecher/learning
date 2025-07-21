
// Rust: W3Schools - Main Tutorial
// Section 20: Borrowing

// To use a value without ownership, we can borrow the value using a reference (&).

fn main() {

    // The example from the last section can be made to work like so:
    let a = String::from("Hello");
    let b = &a;

    println!("a = {}", a);
    println!("b = {}", b);

    // However, if we wish to edit the value, we must use a mutable reference (&mut):
    let mut name = String::from("John");
    let name_ref = &mut name;
    name_ref.push_str(" Doe");
    // println!("{}", name); // Error: cannot borrow `name` as immutable because it is also borrowed as mutable.
    println!("{}", name_ref);
}
