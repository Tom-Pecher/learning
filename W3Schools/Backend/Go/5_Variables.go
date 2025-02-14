
// Go: W3Schools - Main Tutorial
// Section 5: Variables

package main
import ("fmt")

func main() {
	// We define variables using the var keyword and a data type:
	var student string = "John"

	// We can also define variables and infer their data type using the := operator:
	z := 2
  
	fmt.Println(student)
	fmt.Println(z)

	// Declaring variables without a value:
	var a string
	var b int
	var c bool

	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)

	// Assigning values to variables:
	a = "Hello"
	fmt.Println(a)

	// Declare and assign values to multiple variables:
	var x, y = 6, "Hello"

	fmt.Println(x)
	fmt.Println(y)

	// Multiple variable declarations can also be grouped together into a block for greater readability:
	var (
		d int
		e int = 1
		f string = "hello"
	)

	fmt.Println(d)
	fmt.Println(e)
	fmt.Println(f)
}