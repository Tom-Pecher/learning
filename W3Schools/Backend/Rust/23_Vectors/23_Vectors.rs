
// Rust: W3Schools - Main Tutorial
// Section 23: Vectors


fn main() {

    // We can make a vector with the vec! macro:
    let fruits = vec!["apple", "banana", "orange"];

    // We can access elements of a vector by index:
    println!("The first fruit is {}", fruits[0]);

    // We can also get the length of a vector:
    println!("There are {} fruits in the vector", fruits.len());

    // We can also loop over the vector by passing a reference to it:
    for fruit in &fruits {
        println!("The fruit is {}", fruit);
    }

    // To change an element of a vector, we can use the index to access the element, so long as the vector is mutable:
    let mut fruits = vec!["apple", "banana", "orange"];
    fruits[0] = "pear";
    println!("The first fruit is now {}", fruits[0]);

    // To add an element to the end of a vector, we can use the push method:
    fruits.push("grape");
    println!("{:?}", fruits);

    // To remove the last element of a vector, we can use the pop method:
    fruits.pop();
    println!("{:?}", fruits);

    // To insert an element at a specific index, we can use the insert method:
    fruits.insert(1, "banana");
    println!("{:?}", fruits);

    // To remove an element at a specific index, we can use the remove method:
    fruits.remove(1);
    println!("{:?}", fruits);
    
}
