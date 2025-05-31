// Introduction:
// Go is a statically typed, compiled language.
// It is very much like C in terms of performance and low-level features.

// Go is organized into packages.
// The "main" package is the entry point of the program.
package main

// "fmt" is used for formatted I/O (like stdio in C).
import "fmt"

func main() {
	// Variables:
	// You can declare a variable with an explicit type:
	var name string = "ahmed"

	// Or use shorthand declaration with type inference:
	age := 25

	// Constants:
	const PORT int = 5000

	// Print function:
	fmt.Println("Name:", name)
	fmt.Println("Age:", age)
	fmt.Println("Port:", PORT)

	// String Interpolation in GO:
	// %s For Strings
	// %d For Integers
	// %f For Floats
	// %v For Generic Value
	// Using Sprintf
	msg := fmt.Sprintf("Hello, %s!", name)
	fmt.Println(msg)
	// Using Println or Printf
	fmt.Printf("Your name is %s and you are %d years old !", name, age)

	// Input
	var userName string
	fmt.Print("Enter your Name :")
	fmt.Scan(&userName) // Sends the location to prevent copy
	fmt.Printf("Your name is %s", userName)

	// If statement:
	x, y := 10, 5
	if x > y {
		fmt.Println("X is bigger:", x)
	} else {
		fmt.Println("Y is bigger:", y)
	}

	// Loop
	// For loop:
	for i := 0; i < 5; i++ {
		fmt.Println("Hello world!", i)
	}
	// For Each Loop:
	names := []string{"ahmed", "ali", "muhammad"}
	for name := range names {
		fmt.Println(name)
	}

	// Arrays in Go:
	// Static array:
	var arr1 = [3]int{1, 2, 3}
	for i := 0; i < len(arr1); i++ {
		fmt.Println("arr1 element:", arr1[i])
	}

	// Dynamic array (slice):
	arr2 := []int{4, 5, 6}
	for i := 0; i < len(arr2); i++ {
		fmt.Println("arr2 element:", arr2[i])
	}

	// Append to slice:
	arr2 = append(arr2, 7)
	fmt.Println("Updated arr2:", arr2)

	// Create empty slice:
	s := make([]int, 0)
	fmt.Println("Empty slice s:", s)

	// Function call:
	result := add(5, 3)
	fmt.Println("Sum from add():", result)

	// Maps in Go:
	m := map[string]int{
		"ahmed": 20,
		"ali":   0,
	}

	// Check if a key exists:
	val, ok := m["ali"]
	if ok {
		fmt.Println("Found:", val)
	} else {
		fmt.Println("Not Found")
	}

	// Pointers
	// &variableName (returns the location of the variable in memeory!)

}

// Function definition:
func add(a int, b int) int {
	return a + b
}
