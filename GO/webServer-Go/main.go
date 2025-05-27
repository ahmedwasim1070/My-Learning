package main

import (
	"fmt"
	"net/http"
)

func main() {
	// Handler for Root route !
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		http.ServeFile(w, r, "index.html")
	})

	// Start the server
	fmt.Println("Server started at port 8080")
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		fmt.Println("Error starting server : ", err)
	}

}
