
// Rust: W3Schools - Main Tutorial
// Section 24: Tuples


fn main() {

    // We create a tuple using parentheses and commas:
    let person = ("John", 30, true);

    // We can access the elements of the tuple using indexing, however this time we have to use dot notation:
    println!("Name: {}", person.0);
    println!("Age: {}", person.1);
    println!("Is active: {}", person.2);
    
    // We can also use destructuring (unpacking) to access the elements of the tuple:
    let (name, age, is_active) = person;
    println!("Name: {}", name);
    println!("Age: {}", age);
    println!("Is active: {}", is_active);

    // Tuples are often used as return values from functions:
    fn get_user() -> (String, i32) {
        (String::from("Liam"), 25)
    }
    
    let user = get_user();
    println!("User: {} ({} years old)", user.0, user.1);

}
