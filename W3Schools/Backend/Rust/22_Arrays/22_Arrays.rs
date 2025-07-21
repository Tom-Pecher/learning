
// Rust: W3Schools - Main Tutorial
// Section 22: Arrays


fn main() {

    // Arrays are created using square brackets with values separated by commas:
    let numbers = [1, 2, 3, 4, 5];

    // We can access the elements of the array using the index number:
    println!("The first number is: {}", numbers[0]);

    // Likewise, we can also modify the elements of the array but only if the array is mutable:
    let mut numbers = [1, 2, 3, 4, 5];
    numbers[0] = 10;
    println!("The new first number is: {}", numbers[0]);

    // Get the length of the array:
    println!("The length of the array is: {}", numbers.len());

    // To loop through each element of an array, we can use a for loop with the in keyword:
    let fruits = ["apple", "banana", "orange"];
    for fruit in fruits {
        println!("I like {}.", fruit);
    }

    // To print an entire array as-is, we can use the {:?} format specifier:
    let numbers = [1, 2, 3, 4, 5];
    println!("{:?}", numbers); 
    
}
