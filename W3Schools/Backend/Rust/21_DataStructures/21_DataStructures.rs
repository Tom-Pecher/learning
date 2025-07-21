
// Rust: W3Schools - Main Tutorial
// Section 21: Data Structures

// Import the HashMap data type:
use std::collections::HashMap;

fn main() {

    // Arrays are immutable, fixed length collections of elements of the same type:
    let fruits = ["apple", "banana", "orange"];
    println!("Last fruit: {}", fruits[2]); 

    // Vectors are mutable, growable collections of elements of the same type:
    let mut numbers = vec![1, 2, 3];
    numbers.push(4);
    println!("Last number: {}", numbers[3]);

    // Tuples are immutable, fixed length collections of elements of different types:
    let person = ("John", 30, true);
    println!("Name: {}", person.0);
    println!("Age: {}", person.1);
    println!("Is active: {}", person.2); 

    // Hash maps are mutable, key-value collections of elements of different types:
    let mut scores = HashMap::new();
    scores.insert("Alice", 10);
    scores.insert("Bob", 20);
    println!("Score for Alice: {}", scores["Alice"]);
    println!("Score for Bob: {}", scores["Bob"]);

}
