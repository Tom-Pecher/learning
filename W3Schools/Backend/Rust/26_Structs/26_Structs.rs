
// Rust: W3Schools - Main Tutorial
// Section 26: Structs


// Structures are custom data types that allow you to group related data together:
struct Person {
    name: String,
    age: u32,
    can_vote: bool,
  }

fn main() {

    // We can create an instance of a struct by specifying the values for each field:
    let user = Person {
        name: String::from("John"),
        age: 35,
        can_vote: true,
    };
    
    println!("Name: {}", user.name);
    println!("Age: {}", user.age);
    println!("Can vote? {}", user.can_vote); 

}
