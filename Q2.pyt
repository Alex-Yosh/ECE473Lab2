#inital position
import copy

class Node:
    def __init__(self, currentStones, oppStone, oppTurn: bool ,depth):
        # self.value = value  # The value of the node
        # self.nextNodes = NextNodes 
        self.currConfig = currentStones
        self.opponentConfig = oppStone
        self.depth = depth
        self.oppTurn = oppTurn
        self.evalation = self.EvaluationFunction()

        if (depth < 3):
            self.nextNodes = self.AllNextNodes(self.currConfig, self.opponentConfig, self.oppTurn, self.depth)

    def AllNextNodes(self, currentStones, oppStones, oppTurn: bool, depth):
        moves = []
        for i in range(0, 4):
            for j in range(0, 4):
                if (oppTurn):
                    if (currentStones[i][j] > 0 or oppStones[i][j] == 0):
                        continue
                    
                    if (self.MoveLeft(oppStones, currentStones, i, j) != None):
                        moves.append(Node(currentStones, self.MoveLeft(oppStones, currentStones, i, j), not oppTurn, depth + 1))

                    if (self.MoveRight(oppStones, currentStones, i, j) != None):
                        moves.append(Node(currentStones, self.MoveRight(oppStones, currentStones, i, j), not oppTurn, depth + 1))

                    if (self.MoveUp(oppStones, currentStones, i, j) != None):
                        moves.append(Node(currentStones, self.MoveUp(oppStones, currentStones, i, j), not oppTurn, depth + 1))

                    if (self.MoveDown(oppStones, currentStones, i, j) != None):
                        moves.append(Node(currentStones, self.MoveDown(oppStones, currentStones, i, j), not oppTurn, depth + 1))
                else:
                    if (oppStones[i][j] > 0 or currentStones[i][j] == 0):
                        continue

                    if (self.MoveLeft(currentStones, oppStones, i, j) != None):
                        moves.append(Node(self.MoveLeft(currentStones, oppStones, i, j), oppStones, not oppTurn, depth + 1))

                    if (self.MoveRight(currentStones, oppStones, i, j) != None):
                        moves.append(Node(self.MoveRight(currentStones, oppStones, i, j), oppStones, not oppTurn, depth + 1))

                    if (self.MoveUp(currentStones, oppStones, i, j) != None):
                        moves.append(Node(self.MoveUp(currentStones, oppStones, i, j), oppStones, not oppTurn, depth + 1))

                    if (self.MoveDown(currentStones, oppStones, i, j) != None):
                        moves.append(Node(self.MoveDown(currentStones, oppStones, i, j), oppStones, not oppTurn, depth + 1))

        return moves


    def MoveUp(self, currentStones, oppStones, i, j):
        if i != 0:
            stones = currentStones[i][j]
            move = copy.deepcopy(currentStones)
            increment = 1
            while oppStones[i-increment][j] == 0 and i-increment > 0 and stones > 0:
                if (increment < stones):
                    move[i-increment][j] += increment
                    stones-=increment
                else:
                    #rest of stones
                    move[i-increment][j] += stones
                    stones = 0
                increment+=1

            if (move != currentStones or (increment == 1 and oppStones[i-increment][j] == 0)):
                move[i - increment + (oppStones[i-increment][j] != 0)][j] += stones
                move[i][j] = 0
                return move
            
    def MoveDown(self, currentStones, oppStones, i, j):
        if i != 3:
            stones = currentStones[i][j]
            move = copy.deepcopy(currentStones)
            increment = 1
            while oppStones[i+increment][j] == 0 and i+increment < 3 and stones > 0:
                if (increment < stones):
                    move[i+increment][j] += increment
                    stones-=increment
                else:
                    #rest of stones
                    move[i+increment][j] += stones
                    stones = 0
                increment+=1

            if (move != currentStones or (increment == 1 and oppStones[i+increment][j] == 0)):
                move[i + increment - (oppStones[i+increment][j] != 0)][j] += stones
                move[i][j] = 0
                return move
    
    def MoveLeft(self, currentStones, oppStones, i, j):
        if j != 0:
            stones = currentStones[i][j]
            move = copy.deepcopy(currentStones)
            increment = 1
            while oppStones[i][j-increment] == 0 and j-increment > 0 and stones > 0:
                if (increment < stones):
                    move[i][j-increment] += increment
                    stones -= increment
                else:
                    #rest of stones
                    move[i][j-increment] += stones
                    stones = 0
                increment+=1

            if (move != currentStones or (increment == 1 and oppStones[i][j-increment] == 0)):
                move[i][j - increment + (oppStones[i][j-increment] != 0)] += stones
                move[i][j] = 0
                return move
            
    def MoveRight(self, currentStones, oppStones, i, j):
        if j != 3:
            stones = currentStones[i][j]
            move = copy.deepcopy(currentStones)
            increment = 1
            while oppStones[i][j+increment] == 0 and j+increment < 3 and stones > 0:
                if (increment < stones):
                    move[i][j+increment] += increment
                    stones-=increment
                else:
                    #rest of stones
                    move[i][j+increment] += stones
                    stones = 0
                increment+=1

            if (move != currentStones or (increment == 1 and oppStones[i][j+increment] == 0)):
                move[i][j + increment - (oppStones[i][j+increment] != 0)] += stones
                move[i][j] = 0
                return move
            
    def EvaluationFunction(self):
        #Idea 1: How many moves do I have left
        e = 0

        # for i in range(0, 4):
        #     for j in range(0, 4):
        #             if (self.currConfig[i][j] > 0):
        #                 if (self.MoveLeft(self.currConfig, self.opponentConfig, i, j) != None):
        #                     e+=1

        #                 if (self.MoveRight(self.currConfig, self.opponentConfig, i, j) != None):
        #                     e+=1

        #                 if (self.MoveUp(self.currConfig, self.opponentConfig, i, j) != None):
        #                     e+=1

        #                 if (self.MoveDown(self.currConfig, self.opponentConfig, i, j) != None):
        #                     e+=1
        #             elif(self.opponentConfig[i][j] > 0):
        #                 if (self.MoveLeft(self.opponentConfig, self.currConfig, i, j) != None):
        #                     e-=1

        #                 if (self.MoveRight(self.opponentConfig, self.currConfig, i, j) != None):
        #                     e-=1

        #                 if (self.MoveUp(self.opponentConfig, self.currConfig, i, j) != None):
        #                     e-=1

        #                 if (self.MoveDown(self.opponentConfig, self.currConfig, i, j) != None):
        #                     e-=1

        # return e
    
        #Idea 2: How many spaces do I take up

        for i in range(0, 4):
            for j in range(0, 4):
                if (self.currConfig[i][j] > 0):
                    e+=1
                elif(self.opponentConfig[i][j] > 0):
                    e-=1

        printBoard(self.currConfig, self.opponentConfig)
        print(e)
        return e
    

        
        


class Player:
    def __init__(self, isWhite = True):
        self.stones = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        if (isWhite):
            self.stones[0][0] = 10
        else:
            self.stones[3][3] = 10

            
    # given possbile next move, get all terminal values
    def findTerminals(self, otherPlayer):
        # i = 0, j = 0
        depth = 1
        curNode = Node(self.stones, otherPlayer.stones, False, depth)
        # myTurn = False
        # while(curNode.nextNodes != []):
        #     depth+=1
        #     curNode = []
        #     if (myTurn):
        #         for config in currentMoves:
        #             currentMoves += config.movesForTile[0][0]
                
        #         myTurn = False
        #     else:

        #         myTurn = True

    

    

#helper functions
def printBoard(configWhite, configBlack):
    for i in range(0,4):
        line = ""
        for j in range(0,4):   
            if (configWhite[i][j]>0):
                line += "w" + str(configWhite[i][j])
            elif (configBlack[i][j]>0):
                line += "b" + str(configBlack[i][j])
            else:
                line += "e"
            line += " "
        print(line + "\n")

#main code
black = Player(isWhite = False)
black.stones[2][2] = 8
white = Player()
white.findTerminals(otherPlayer=black)





