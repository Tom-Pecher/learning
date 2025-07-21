
// Rust: W3Schools - Main Tutorial
// Section 18: Strings


// Strings are use to store text like in any language.
// However, in Rust strings are a little more complicated.


fn main() {

    // There are two main types of strings in Rust, string slices (&str) which are immutable:
    let greeting1: &str = "Hello";
    println!("{}", greeting1); 

    // And Strings, which are mutable:
    let greeting2 = "Hello".to_string(); 
    println!("{}", greeting2);

    // To add text to a string, we can use the push_str() method:
    let mut greeting = String::from("Hello");
    greeting.push_str(" World");
    println!("{}", greeting);

    // To add a single character to a string, we can use the push() method:
    let mut word = String::from("Hi");
    word.push('!');
    println!("{}", word); // Hi! 

    // To concatenate strings, we can use the + operator:
    let word1 = String::from("Hello");
    let word2 = String::from("World");
    let word3 = word1 + " " + &word2;
    println!("{}", word3);

    // Or we can use the format! macro (preferred):
    let s1 = String::from("Hello");
    let s2 = String::from("World!");
    let s3 = String::from("What a beautiful day!");
    let result = format!("{} {} {}", s1, s2, s3);
    println!("{}", result);

    // To get a string's length, we can use the len() method:
    let s = String::from("Hello");
    println!("{}", s.len());
    
}
