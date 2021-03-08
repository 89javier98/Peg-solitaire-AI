# board: variable saving the characters matrix (state of the game)

# Standard self.size chosen

# void print(): show the board
# boolean onLimits(int r, int c): position is on limits
# boolean noMoves(): no pieces to move
# boolean movable(int r, int c, int dir): piece can be moved in such direction
# boolean movable(int r, int c): piece can be moved
# void move(args?): move a piece (if possible)

#If the self.size = 7

class Board:
    "Board of the Peg-Solitaire game. Matrix of characters."
    board = []
    size = 7



    def __init__(self):
        #IDK why, but have to declare it twice
        def onLimits(self, r, c):
            rOutOfLimits = r < (self.size-1)/3 or r > (2*(self.size-1))/3
            cOutOfLimits = c < (self.size-1)/3 or c > (2*(self.size-1))/3
            return not(rOutOfLimits and cOutOfLimits)

        #Creating the board:
        for r in range(self.size):
            row = []
            for c in range(self.size):
                if not onLimits(self, r,c):
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


    #Returns the matrix
    def state(self):
        return self.board

    #Tells if the position is inside the board
    def onLimits(self, r, c):
        "Checks if row r, column c are inside the board"
        rOutOfLimits = r < (self.size-1)/3 or r > (2*(self.size-1))/3
        cOutOfLimits = c < (self.size-1)/3 or c > (2*(self.size-1))/3
        return not(rOutOfLimits and cOutOfLimits)

    #Piece can be move in such direction
    # 1: Up. 2: Righ. 3: Down. 4: Left
    def movable(self, r, c, dir):
        """Checks if it is able to move a piece in certain direction.
        1 = Up, 2 = Right, 3 = Down, 4 = Left"""
        mov = False
        if   dir == 1:
            if self.onLimits(r-1, c) and self.onLimits(r-2, c): #To avoid index error in lists
                if self.board[r-1][c] == 'O' and self.board[r-2][c] == 'X':
                    mov = True
        
        elif dir == 2:
            if self.onLimits(r, c+1) and self.onLimits(r, c+2):
                if self.board[r][c+1] == 'O' and self.board[r][c+2] == 'X':
                    mov = True
        
        elif dir == 3:
            if self.onLimits(r+1, c) and self.onLimits(r+2, c):
                if self.board[r+1][c] == 'O' and self.board[r+2][c] == 'X':
                    mov = True

        elif dir == 4:
            if self.onLimits(r, c-1) and self.onLimits(r, c-2):
                if self.board[r][c-1] == 'O' and self.board[r][c-2] == 'X':
                    mov = True
        return mov