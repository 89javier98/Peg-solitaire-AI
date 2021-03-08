#File testing the project
from Board import *

board1 = Board()

def assertTrue(x):
    "Used for testing. Passed if x == True"
    if(x):
        print("Passed")
    else:
        print("Failed")

def assertFalse(x):
    "Used for testing. Passed if x == False"
    if(not x):
        print("Passed")
    else:
        print("Failed")


#Checking initial board
board1.print()

#Testing onLimits()
assertFalse(board1.onLimits(0,0))
assertFalse(board1.onLimits(0,1))
assertFalse(board1.onLimits(1,0))
assertFalse(board1.onLimits(1,1))
assertFalse(board1.onLimits(1,5))
assertFalse(board1.onLimits(1,6))


#Testing the 4 first pieces: the 4 initial possible moves
assertTrue(board1.movable(5, 3, 1))
assertTrue(board1.movable(3, 1, 2))
assertTrue(board1.movable(1, 3, 3))
assertTrue(board1.movable(3, 5, 4))

