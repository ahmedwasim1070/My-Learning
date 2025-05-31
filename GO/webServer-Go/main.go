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
	PORT := ":8080"
	fmt.Printf("Server started at port %v \n", PORT)
	err := http.ListenAndServe(PORT, nil) //http.ListenAndServe() opens a http port while on left port number and on right it would be like on sucess
	if err != nil {
		fmt.Println("Error starting server : ", err)
	}

}
