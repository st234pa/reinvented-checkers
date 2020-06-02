package main

// Import our dependencies. We'll use the standard HTTP library as well as the gorilla router for this app
import (
	"encoding/json"
	"net/http"

	"github.com/gorilla/mux"
)

func main() {
	// Here we are instantiating the gorilla/mux router
	r := mux.NewRouter()

	r.Handle("/hello", NotImplemented).Methods("GET")

	// Our application will run on port 8080. Here we declare the port and pass in our router.
	http.ListenAndServe(":8080", r)

}

// NotImplemented handler. Whenever an API endpoint is hit we will simply return the message "Not Implemented"
var NotImplemented = http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Not Implemented"))
})

// PieceColor represents the color of a checkers piece.
type PieceColor int

const (
	// None = 0
	None PieceColor = iota
	// Black = 1
	Black
	// White = 2
	White
)

func (color PieceColor) String() string {
	return []string{"None", "Black", "White"}[color]
}

// Piece represents a piece or an empty space on a board at (Row, Column).
type Piece struct {
	Row    int
	Column int
	Color  PieceColor
	isKing bool
}

// Checkerboard has an Id number and its size is defined by Rows, the number of rows, and Columns, the number of columns.
// Board[r][c] is a piece or an empty space at row r and column c, for r in [0, Rows) and c in [0, Columns).
type Checkerboard struct {
	ID      int
	Rows    int
	Columns int
	Board   [][]Piece
}

// Initialize a board according to American checkers rules.
func (board Checkerboard) Initialize() Checkerboard {

	for row := 0; row < board.Rows; row++ {
		for column := 0; column < board.Columns; column++ {
			board.Board[row][column] = Piece{Row: row, Column: column, Color: None, isKing: false}
		}
	}
	return board
}

// ModifyBoardHandler will modify a board in the body of a POST request
var ModifyBoardHandler = http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
	var board Checkerboard

	w.Header().Set("Content-Type", "application/json")
	payload, _ := json.Marshal(board)
	w.Write([]byte(payload))

})
