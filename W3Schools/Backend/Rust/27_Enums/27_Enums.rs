
// Rust: W3Schools - Main Tutorial
// Section 27: Enums


// Enums are a way to define a type that can have a limited set of possible values:
enum Direction {
    Up,
    Down,
    Left,
    Right,
}

fn main() {

    // We can create an instance of an enum by specifying the value:
    let my_direction = Direction::Up;
    println!("We are going up!");

    // Enums are especially compatible with match statements:
    match my_direction {
        Direction::Up => println!("We are going up!"),
        Direction::Down => println!("We are going down!"),
        Direction::Left => println!("We are going left!"),
        Direction::Right => println!("We are going right!"),
    }

}
