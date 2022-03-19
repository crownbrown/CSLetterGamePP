# CSPythonGamePP
A Sudoko-like, two-player game implemented by a Python class that creates 4 x 4 game board and tracks the progress of the game. 

Aclass called FourLetterBoard that represents the board for a two-player game that is played on a 4x4 grid. This class does not do everything needed to play a game - it just takes care of the logic for the game board. A turn consists of placing one of the four letters A-D on an empty space of the board. Your class does not keep track of whose turn it is, so it will allow multiple moves by the same player consecutively (things like keeping track of player turn, reading input from the user, and displaying output would belong in another class, but you don't have to worry about that).

If you split the board in half both horizontally and vertically, it separates the board into four 2x2 "regions". The winner is the one who plays the last letter in a row, column, or region that now contains one of each letter - regardless of who played the other letters. A player cannot put a letter in a row, column, or region if the **opponent** has already played that letter in that row, column, or region. Otherwise, a player may duplicate a letter.

The class has the following **private** data members: a representation of the board, and the current state, which holds one of the three following values: "X_WON", "O_WON", "DRAW", or "UNFINISHED". 

It also has an init method that initializes the board to being empty, initializes the current_state to "UNFINISHED", and appropriately initializes any other data members. 

It has a get method named get_current_state, which returns the current state.

It hase a method named make_move that takes four parameters - the row and the column (in that order) of the square being played on, the letter being played there, and either 'x' or 'o' to indicate the player making the move. If the game has already been won or drawn, or if the square is not empty, or if the letter duplicates an opponent letter in the same row, column, or region, make_move returns **False**. Otherwise, it records the move, update the current state, and **returns True**. It detects if the current move causes a win for either player, or a draw. A draw occurs when the board is full, but neither player has won.

As a very simple example, the class be used as follows:
```
board = FourLetterBoard()
board.make_move(0,0,'B','o')  # The o player places a B in one of the corners
board.make_move(3,3,'D','o')  # The o player places a D in the opposite corner
print(board.get_current_state())
```
