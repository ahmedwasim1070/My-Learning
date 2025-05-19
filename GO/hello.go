// Introduction
// Go is an statically typed , compiled language !
// Go is very much like C

// Go is divided into small packages
// Like main Package
package main

// Format package for the Print and Input just like in c like std
// import "fmt"

// Every program should have main() function to work
// In go function is defined by func
func main() {
	// Since Go is static type so yoy gotta define the type of the variable to do that like that
	// var name string = "ahmed"
	// So the short way of doing that is like that it just picks the type based on input

	// name := "ahmed"
	// Print Function
	// fmt.Print(name)

	// Simple Program to descrbe if Statment
	// x, y := 10, 5
	// if x > y {
	// 	fmt.Print("X ig bigger :", x)
	// } else {
	// 	fmt.Print("Y is bigger :", y)
	// }

	// Loop (for loop)
	// for x := 0; x < 5; x++ {
	// 	fmt.Print("Hello world ! ", x, "\n")
	// }

	// Arrays in GO
	// Static Array (size fixed !)
	// var arr [3]int = [3]int{1, 2, 3}
	// or
	// var arr = [3]int{1, 2, 3}
	// or
	// arr := [3]string{"nigga 1", "nigga 2", "nigga 3"}
	// for x := 0; x < len(arr); x++ {
	// 	fmt.Print(arr[x], "\n")
	// }
	// Dynamic Array
	// var arr []int = []int{1, 2, 3}
	// or
	// var arr = []int{1, 2, 3}
	// arr := []string{"nigga 1 ", " nigga 2 ", "nigga 3"}
	// for x := 0; x < len(arr); x++ {
	// 	fmt.Print(arr[x], "\n")
	// }
	// Arrays have some built in functions to like append or popa
	// arr.append(arr,7)   This returns the new array so you store it somewhere
	// s := make([]int, 0)    Where on left []int shows its dynamic and on right it says 0 means for now length is 0

	// Functions
	// func add(a int , b int)int {
	// 	return a + b
	// }

	// Maps
	// var m = map[string]int{
	// 	"ahmed": 20, "ali": 00,
	// }
	// or
	// m := map[string]int{
	// 	"ahmed": 20,
	// 	"ali":   00,
	// }
	// val, ok := m["nigga"]   Way of searching a key in object if there is key you can store it in val
	// if ok {
	// 	fmt.Print("Found :", val)
	// } else {
	// 	fmt.Print("Not Found ")
	// }

}
