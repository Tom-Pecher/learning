
// RUST: Rust By Example
// Section 1: Primitives

// Scalar Types:
    // Signed integers: i8, i16, i32, i64, i128 and isize (pointer size)
    // Unsigned integers: u8, u16, u32, u64, u128 and usize (pointer size)
    // Floating point: f32, f64
    // char Unicode scalar values like 'a', 'α' and '∞' (4 bytes each)
    // bool either true or false
    // The unit type (), whose only possible value is an empty tuple: ()

// Compound Types:
    // Arrays like [1, 2, 3]
    // Tuples like (1, true)

// Variables can always be type annotated. 
// Numbers may additionally be annotated via a suffix or by default. 
// Integers default to i32 and floats to f64:
fn main() {
    // Variables can be type annotated:
    let _logical: bool = true;

    let _a_float: f64 = 1.0;  // Regular annotation
    let _an_integer = 5i32; // Suffix annotation

    // Or a default will be used:
    let _default_float = 3.0; // `f64`
    let _default_integer = 7;   // `i32`

    // A type can also be inferred from context:
    let mut _inferred_type = 12; // Type i64 is inferred from another line.
    _inferred_type = 4294967296i64;

    // A mutable variable's value can be changed:
    let mut _mutable = 12; // Mutable `i32`
    _mutable = 21;

    // The type of a variable can't be changed:
    // mutable = true;

    // Variables can be overwritten with shadowing:
    let _mutable = true;

    // Array signature consists of Type T and length as [T; length]:
    let _my_array: [i32; 5] = [1, 2, 3, 4, 5];

    // Tuple is a collection of values of different types 
    // and is constructed using parentheses ():
    let _my_tuple = (5u32, 1u8, true, -5.04f32);
}
