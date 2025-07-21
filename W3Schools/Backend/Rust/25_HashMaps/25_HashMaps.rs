
// Rust: W3Schools - Main Tutorial
// Section 25: Hash Maps


// To use the hash map functionality, we need to import the HashMap module:
use std::collections::HashMap;

fn main() {

    // Create a new hash map:
    let mut capital_cities = HashMap::new();

    // Add keys and values:
    capital_cities.insert("England", "London");
    capital_cities.insert("Germany", "Berlin");
    capital_cities.insert("Norway", "Oslo");

    // Print the hash map:
    println!("{:?}", capital_cities);

    // Access a value in the hash map:
    let value = capital_cities.get("England");
    println!("{:?}", value);

    // The shorthand for this is as follows:
    let value = capital_cities["England"];
    println!("{:?}", value);

    // We cannot simply print this, since it is of type Option<&String>, hence:        
    if let Some(city) = capital_cities.get("England") {
        println!("The capital of England is {}.", city);
    } else {
        println!("England is not in the map.");
    } 

    // We can iterate over a hash map using tuples:
    for (key, value) in &capital_cities {
        println!("The capital of {} is {}", key, value);
    }

    // If you insert a new value using a key that already exists, the old value is replaced with the new one:
    capital_cities.insert("England", "Manchester");
    println!("{:?}", capital_cities);

    // To remove entries, we use the remove method:
    capital_cities.remove("England");
    println!("{:?}", capital_cities); 

}
