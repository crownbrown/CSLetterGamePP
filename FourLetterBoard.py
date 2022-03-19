# Author: Steve Thatcher
# Date: 03-10-2021
# Description: This file contains a class ("FourLetterBoard") that initializes a game board and key variables, and then a make_move method that, in concert with other methods, validates moves, records moves, checks for possible wins/draw

class FourLetterBoard:
    """This class initializes key variables, and contains several methods that, among other things, record turns, return current state and board, validate moves and wins by row, column, and region"""
    def __init__(self, current_row=int(), current_column=int(), current_letter=str(), current_player=str()):
        self._current_row = current_row
        self._current_column = current_column
        self._current_letter = current_letter
        self._current_player = current_player
        self._board = [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]] #Initializes an empty board of four rows and fours columns
        self._current_state = "UNFINISHED" #states the beginning game state to "Unfinisihed"

    def record_move_to_board(self, current_row, current_column, current_letter, current_player):
        """Records the current move to the board"""
        self._board[current_row][current_column] = current_letter + current_player

    def get_current_state(self):
        """Returns the current state of the game - either WIN, DRAW, or UNFINISHED"""
        return self._current_state

    def get_current_board(self):
        """Returns the current game board"""
        return self._board

    def change_current_state(self, current_player):
        """Changes the current game state to a win for the current player"""
        if current_player == "x":
            self._current_state = "X_WON"
        if current_player == "o":
            self._current_state = "O_WON"

    def change_current_state_draw(self):
        """Change the current game state to a draw"""
        self._current_state = "DRAW"


    def row_opponent_move_check(self, current_row, opponent_move):
        """Checks the current row to see if the opponent has a move that would prevent the current move from being played"""
        if opponent_move not in self._board[current_row]:
            return True
        else:
            return False

    def column_opponent_move_check(self, current_column, opponent_move, column_check):
        """Checks the current column to see if the opponent has a move that would prevent the current move from being played"""
        if opponent_move not in column_check:
            return True
        else:
            return False

    def region_opponent_move_check(self, current_row, current_column, opponent_move, region_check):
        """Checks the current region to see if the opponent has a move that would prevent the current move from being played"""
        if current_row == 0:  # Region Check - Region Row Set
            region_row = 1
        elif current_row == 1:
            region_row = 0
        elif current_row == 2:
            region_row = 3
        elif current_row == 3:
            region_row = 2

        if current_column == 0:  # Region Check - Region Column Set
            region_column = 1
        elif current_column == 1:
            region_column = 0
        elif current_column == 2:
            region_column = 3
        elif current_column == 3:
            region_column = 2

        region_check.append(self._board[current_row][region_column]) ###Appends the squares in the region to a set for checking
        region_check.append(self._board[region_row][current_column])
        region_check.append(self._board[region_row][region_column])

        if opponent_move not in region_check:
            return True, region_check
        else:
            return False, region_check


    def row_win_check(self, current_row, winning_set, win_check_row_set):
        """Checks the current row to see if the current player has won via the row"""
        for element in self._board[current_row]:
            for char in element:
                if char in winning_set:
                    win_check_row_set.add(char)
        if winning_set == win_check_row_set:
            return True


    def column_win_check(self, winning_set, column_check, win_check_column_set):
        """Checks the current column to see if the current player has won via the row"""
        for element in column_check:
            for char in element:
                if char in winning_set:
                    win_check_column_set.add(char)
        if winning_set == win_check_column_set:
            return True

    def region_win_check(self, winning_set, region_check, win_check_region_set):
        """Checks the current region to see if the current player has won via the row"""
        for element in region_check:
            for char in element:
                if char in winning_set:
                    win_check_region_set.add(char)
        if winning_set == win_check_region_set:
            return True

    def make_move(self, current_row, current_column, current_letter, current_player):
        """Checks to see that the game is unfinished, then checks to see if the current move square is empty, then calls other methods to check the move and for possible win/draw"""
        if self._current_state == "UNFINISHED": #Checks that the current state of the game is unfinished

            if self._board[current_row][current_column] == "": #Checks to see that the current move is played in an empty square

                if current_player == "o": #Creates a variable for the opponent player based on the current player
                    opponent_player = "x"
                elif current_player == "x":
                    opponent_player = "o"

                opponent_move = current_letter + opponent_player #Creates a variable from the current player's chosen letter and their opponent's player name


                column_check = [element[current_column] for element in self._board] #Creates a list of the current elements in the current column for checking existing moves in that column


                region_check = [] #Creates an empty list to pass for checking regions

                if self.row_opponent_move_check(current_row, opponent_move): #calls the method for checking the current row to validate the current move
                    if self.column_opponent_move_check(current_column, opponent_move, column_check): #calls the method for checking the current column to validate the current move
                        if self.region_opponent_move_check(current_row, current_column, opponent_move, region_check): #calls the method for checking the current region to validate the current move
                            self.record_move_to_board(current_row, current_column, current_letter, current_player) #calls the method for recording the move if the move was validated by row, column, and region by the methods above

                column_check = [element[current_column] for element in self._board] #creates a current version of column check that includes the current move

                region_check.append(self._board[current_row][current_column]) #appends the current move to the region check list


                winning_set = {'A', 'B', 'C', 'D'} #Creates a winning set of letter for comparison
                win_check_row_set = set() #create empty set for checking row win
                win_check_column_set = set() #create empty set for checking column win
                win_check_region_set = set() #create empty set for checking region win

                if self.row_win_check(current_row, winning_set, win_check_row_set): #calls method for checking win via current row
                    self.change_current_state(current_player) #if win is found in current row, calls method to change game state to win for current player
                if self.column_win_check(winning_set, column_check, win_check_column_set): #calls method for checking win via current column
                    self.change_current_state(current_player) #if win is found in current column, calls method to change game state to win for current player
                if self.region_win_check(winning_set, region_check, win_check_region_set): #calls method for checking win via current region
                    self.change_current_state(current_player) #if win is found in current region, calls method to change game state to win for current player

                draw_check = 0 #creates variable to check for possible draw
                for element in self._board:
                    for turn in element:
                        if turn != "": #checks to see if each square of the board is NOT empty
                            draw_check += 1 #add 1 to draw count if the given square is NOT empty

                if draw_check == 16: #check to see if the draw count is equal to 16
                    self.change_current_state_draw() #if so, it set the game to draw
                else:
                    return True

            else:
                return False

        else:
            return False

#board = FourLetterBoard()

#board.make_move(0,0,'A','o')  #Draw check
#board.make_move(0,1,'C','o')  #
#board.make_move(0,2,'B','o')  #
#board.make_move(0,3,'A','o')  #
#board.make_move(1,0,'A','o')  #
#board.make_move(1,1,'C','o')  #
#board.make_move(1,2,'B','o')  #
#board.make_move(1,3,'A','o')  #
#board.make_move(2,0,'A','o')  #
#board.make_move(2,1,'C','o')  #
#board.make_move(2,2,'B','o')  #
#board.make_move(2,3,'A','o')  #
#board.make_move(3,0,'A','o')  #
#board.make_move(3,1,'C','o')  #
#board.make_move(3,2,'B','o')  #
#board.make_move(3,3,'A','o')  #


#board.make_move(2,0,'D','o')  #Region win
#board.make_move(2,1,'C','o')  #
#board.make_move(3,0,'B','o')  #
#board.make_move(3,1,'A','o')  #

#board.make_move(1,0,'D','o')  #Row win
#board.make_move(1,1,'C','o')  #
#board.make_move(1,2,'B','o')  #
#board.make_move(1,3,'A','o')  #

#board.make_move(0,2,'D','x')  #Column win
#board.make_move(1,2,'C','x')  #
#board.make_move(2,2,'B','x')  #
#board.make_move(3,2,'A','x')  #

#board.make_move(0,2,'A','o')  #
#board.make_move(0,2,'A','x')  #Same square check
#board.make_move(1,2,'B','x')  #
#board.make_move(2,2,'A','x')  #
#board.make_move(3,2,'D','x')  #
#board.make_move(0,0,'A','x')  #Row check
#board.make_move(1,0,'B','x')  #
#board.make_move(0,0,'B','o')  #Region check (0)
#board.make_move(3,3,'C','o')  #Region check (3)
#board.make_move(0,3,'B','o')  #Region check (1)
#board.make_move(3,1,'C','x')  #
#board.make_move(2,0,'C','o')  #

#print(board.get_current_board())
#print(board.get_current_state())