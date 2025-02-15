
// Go: W3Schools - Main Tutorial
// Section 6: Constants

package main
import ("fmt")

// Constants are immutable values, declared with the const keyword:
const PI = 3.14

func main() {
	fmt.Println(PI)

	// There are two types of constants. The first are typed constants, which are defined with a specific type:
	const A int = 1
	fmt.Println(A)

	// The second type of constant is untyped, which is defined without a specific type:
	const B = 2
	fmt.Println(B)
}