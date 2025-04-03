
// RUST: Rust By Example
// Section 1.3: Formatted Print

// Different ways to format/print text:
    // format!: write formatted text to String
    // print!: same as format! but the text is printed to the console (io::stdout).
    // println!: same as print! but a newline is appended.
    // eprint!: same as print! but the text is printed to the standard error (io::stderr).
    // eprintln!: same as eprint! but a newline is appended.

fn main() {
    // The placeholder `{}` indicates where a value will go:
    println!("{} days", 31);

    // Positional arguments can be used to specify order:
    println!("{0}, this is {1}. {1}, this is {0}", "Alice", "Bob");

    // As can named arguments:
    println!("{subject} {verb} {object}",
             object="the lazy dog",
             subject="the quick brown fox",
             verb="jumps over");

    // Different formatting can be invoked by specifying the format character:
    println!("Base 10:               {}",   69420); // 69420
    println!("Base 2 (binary):       {:b}", 69420); // 10000111100101100
    println!("Base 8 (octal):        {:o}", 69420); // 207454
    println!("Base 16 (hexadecimal): {:x}", 69420); // 10f2c

    // You can right-justify text with a specified width. This will output "    1":
    println!("{number:>5}", number=1);

    // You can pad numbers with extra zeroes:
    println!("{number:0>5}", number=1); // 00001

    // We can left-adjust by flipping the sign:
    println!("{number:0<5}", number=1); // 10000

    // You can use named arguments in the format specifier by appending a `$`:
    println!("{number:0>width$}", number=1, width=5);

    // Activity 1:
    // Rust even checks to make sure the correct number of arguments are used.
    println!("My name is {0}, {1} {0}", "Bond", "James");
    // FIXME ^ Add the missing argument: "James"

    // Activity 2:
    // Only types that implement fmt::Display can be formatted with `{}`. User-
    // defined types do not implement fmt::Display by default.
    #[allow(dead_code)] // disable `dead_code` which warn against unused module
    struct Structure(i32);

    // This will not compile because `Structure` does not implement
    // fmt::Display.
    // println!("This struct `{}` won't print...", Structure(3));
    // TODO ^ Try uncommenting this line

    // For Rust 1.58 and above, you can directly capture the argument from a
    // surrounding variable. Just like the above, this will output
    // "    1", 4 white spaces and a "1".
    let number: f64 = 1.0;
    let width: usize = 5;
    println!("{number:>width$}");

    // Activity 3:
    println!("Pi is roughly {pi:.precision$}", pi=std::f64::consts::PI, precision=7);
}
