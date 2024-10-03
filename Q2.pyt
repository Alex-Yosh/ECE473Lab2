#inital position
import copy

class Direction:
    UP = 0
    DOWN = 1
    RIGHT = 2
    LEFT = 3


class Player:
    def __init__(self, isWhite = True):
        self.stones = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        if (isWhite):
            self.stones[0][0] = 10
        else:
            self.stones[3][3] = 10

            

    def findMoves(self, otherPlayer):
        moves = []
        for i in range(0, 3):
            for j in range(0,3):
                if self.stones[i][j] > 0:
                    #up
                    moves.append()
    

    def movesForTile(self, otherPlayer, i, j):

        if (otherPlayer.stones[i][j] > 0):
            return []

        moves = []


        #up
        if i != 0:
            stones = self.stones[i][j]
            move = copy.deepcopy(self.stones)
            increment = 1
            while otherPlayer.stones[i-increment][j] == 0 and i-increment > 0 and stones > 0:
                if (increment < stones):
                    move[i-increment][j] += increment
                    stones-=increment
                else:
                    #rest of stones
                    move[i-increment][j] += stones
                    stones = 0
                increment+=1

            if (move != self.stones):
                move[i-increment+1][j] += stones
                move[i][j] = 0
                moves.append(move)
        return moves


#helper functions
def printBoard(white: Player, black: Player):
    for i in range(0,4):
        line = ""
        for j in range(0,4):   
            if (white.stones[i][j]>0):
                line += "w" + str(white.stones[i][j])
            elif (black.stones[i][j]>0):
                line += "b" + str(black.stones[i][j])
            else:
                line += "e"
            line += " "
        print(line + "\n")

#main code
black = Player(isWhite = False)
black.stones[3][0] = 8
white = Player()
print (black.movesForTile(otherPlayer=white,i= 3,j= 0))

printBoard(white, black)




