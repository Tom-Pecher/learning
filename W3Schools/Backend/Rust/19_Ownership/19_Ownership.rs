
// Rust: W3Schools - Main Tutorial
// Section 19: Ownership


// Ownership is one of the the most important concepts in Rust and what makes it so memory safe.
// Ownership rules for non-primitive types are:
// 1. Each value in Rust has a variable that's called its owner.
// 2. There can only be one owner at a time (but there can be multiple viewers/references).
// 3. When the owner goes out of scope, the value will be dropped.


fn main() {

    // In works since 5 is a primitive type, which are always copied even in this example:
    let a = 5;
    let b = a;
    println!("a = {}", a);  // Works
    println!("b = {}", b);  // Works

    // Conversely, the following will not work since the ownership has been passed to b, hence a has been deleted:
    let a = String::from("Hello");
    let b = a;
    // println!("{}", a); Error: a no longer owns the value
    println!("{}", b); // Ok: b now owns the value 

    // To fix this, we can clone the value:
    let a = String::from("Hello");
    let b = a.clone();
    println!("{}", a); // Ok: a still owns the value
    println!("{}", b); // Ok: b now owns the value

}

// This is why Rust is so fast and memory safe despite not having a garbage collector.
