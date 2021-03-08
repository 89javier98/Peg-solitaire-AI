# board: variable saving the characters matrix (state of the game)

# Standard self.size chosen

# void print(): show the board
# boolean onLimits(int r, int c): position is on limits
# boolean noMoves(int r, int c): piece can be moved
# boolean noMoves(): no piece can be moved
# void move(args?): move a piece (if possible)

#If the self.size = 7

class Board:

    board = []
    size = 7

    def __init__(self):
        for r in range(self.size):
        #Create string
            row = []
            for c in range(self.size):
                rOutOfLimits = r < (self.size-1)/3 or r > (2*(self.size-1))/3
                cOutOfLimits = c < (self.size-1)/3 or c > (2*(self.size-1))/3
                if rOutOfLimits and cOutOfLimits:
                    row.append(' ')
                else:
                    row.append('O')
            self.board.append(row)
        self.board[3][3] = 'X'
        
        

    def print(self):
        for x in self.board:
            row = ""
            for y in x:
                row = row + y + ' '
            print(row)
