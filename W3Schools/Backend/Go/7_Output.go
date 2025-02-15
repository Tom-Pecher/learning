
// Go: W3Schools - Main Tutorial
// Section 7: Output

package main
import ("fmt")

func main() {
  var i,j string = "Hello","World"

  // The Print() function prints its arguments with their default format:
  fmt.Print(i)
  fmt.Print(j)

  // Add newline to ends of Print() statements:
  fmt.Print(i, "\n")
  fmt.Print(j, "\n")

  // Or a space:
  fmt.Print(i, " ", j)

  // The Println() function prints its arguments with a space between each argument and a newline at the end:
  fmt.Println(i)
  fmt.Println(j)

  // The Printf() function formats its arguments according to a format specifier, and returns the resulting string:
  fmt.Printf("%s %s\n", i, j)
}