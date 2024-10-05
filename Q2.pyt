#inital position
import copy
import random

class Node:
    def __init__(self, currentStones, oppStone, oppTurn: bool, depth, alpha = float('-inf'), beta = float('inf'), minimax = True, depthLimit = 3):
        # self.value = value  # The value of the node
        self.currConfig = currentStones
        self.opponentConfig = oppStone
        self.depth = depth
        self.oppTurn = oppTurn
        self.alpha = alpha
        self.beta = beta
        self.depthLimit = depthLimit
        if (minimax):
            self.evalation = self.EvaluationFunction()

        if (depth < depthLimit+1 and minimax):
            self.nextNodes = self.AllNextMinimaxNodes(self.currConfig, self.opponentConfig, self.oppTurn, self.depth)
        
        if (depth == 1 and not minimax):
            self.nextNodes = self.AllNextNodes(self.currConfig, self.opponentConfig, self.oppTurn, self.depth)


    #applys alpha-beta proning
    def AllNextMinimaxNodes(self, currentStones, oppStones, oppTurn: bool, depth):
        moves = []
        for i in range(0, 4):
            for j in range(0, 4):
                if (oppTurn):
                    #minimizer
                    if (currentStones[i][j] > 0 or oppStones[i][j] == 0):
                        continue
                    
                    if (self.MoveLeft(oppStones, currentStones, i, j) != None):
                        n = Node(currentStones, self.MoveLeft(oppStones, currentStones, i, j), not oppTurn, depth + 1, self.alpha, self.beta, depthLimit=self.depthLimit)
                        if (self.ShouldPrune(n)):
                            return moves
                        else:
                            moves.append(n)

                    if (self.MoveRight(oppStones, currentStones, i, j) != None):
                        n = Node(currentStones, self.MoveRight(oppStones, currentStones, i, j), not oppTurn, depth + 1, self.alpha, self.beta, depthLimit=self.depthLimit)
                        if (self.ShouldPrune(n)):
                            return moves
                        else:
                            moves.append(n)

                    if (self.MoveUp(oppStones, currentStones, i, j) != None):
                        n = Node(currentStones, self.MoveUp(oppStones, currentStones, i, j), not oppTurn, depth + 1, self.alpha, self.beta, depthLimit=self.depthLimit)
                        if (self.ShouldPrune(n)):
                            return moves
                        else:
                            moves.append(n)

                    if (self.MoveDown(oppStones, currentStones, i, j) != None):
                        n = Node(currentStones, self.MoveDown(oppStones, currentStones, i, j), not oppTurn, depth + 1, self.alpha, self.beta, depthLimit=self.depthLimit)
                        if (self.ShouldPrune(n)):
                            return moves
                        else:
                            moves.append(n)

                    if (self.MoveDownLeft(oppStones, currentStones, i, j) != None):
                        n = Node(currentStones, self.MoveDownLeft(oppStones, currentStones, i, j), not oppTurn, depth + 1, self.alpha, self.beta, depthLimit=self.depthLimit)
                        if (self.ShouldPrune(n)):
                            return moves
                        else:
                            moves.append(n)

                    if (self.MoveDownRight(oppStones, currentStones, i, j) != None):
                        n = Node(currentStones, self.MoveDownRight(oppStones, currentStones, i, j), not oppTurn, depth + 1, self.alpha, self.beta, depthLimit=self.depthLimit)
                        if (self.ShouldPrune(n)):
                            return moves
                        else:
                            moves.append(n)

                    if (self.MoveUpLeft(oppStones, currentStones, i, j) != None):
                        n = Node(currentStones, self.MoveUpLeft(oppStones, currentStones, i, j), not oppTurn, depth + 1, self.alpha, self.beta, depthLimit=self.depthLimit)
                        if (self.ShouldPrune(n)):
                            return moves
                        else:
                            moves.append(n)

                    if (self.MoveUpRight(oppStones, currentStones, i, j) != None):
                        n = Node(currentStones, self.MoveUpRight(oppStones, currentStones, i, j), not oppTurn, depth + 1, self.alpha, self.beta, depthLimit=self.depthLimit)
                        if (self.ShouldPrune(n)):
                            return moves
                        else:
                            moves.append(n)

                    
                else:
                    #maximizer
                    if (oppStones[i][j] > 0 or currentStones[i][j] == 0):
                        continue

                    if (self.MoveLeft(currentStones, oppStones, i, j) != None):
                        n = Node(self.MoveLeft(currentStones, oppStones, i, j), oppStones, not oppTurn, depth + 1, self.alpha, self.beta, depthLimit=self.depthLimit)
                        if (self.ShouldPrune(n)):
                            return moves
                        else:
                            moves.append(n)

                    if (self.MoveRight(currentStones, oppStones, i, j) != None):
                        n = Node(self.MoveRight(currentStones, oppStones, i, j), oppStones, not oppTurn, depth + 1, self.alpha, self.beta, depthLimit=self.depthLimit)
                        if (self.ShouldPrune(n)):
                            return moves
                        else:
                            moves.append(n)

                    if (self.MoveUp(currentStones, oppStones, i, j) != None):
                        n = Node(self.MoveUp(currentStones, oppStones, i, j), oppStones, not oppTurn, depth + 1, self.alpha, self.beta, depthLimit=self.depthLimit)
                        if (self.ShouldPrune(n)):
                            return moves
                        else:
                            moves.append(n)

                    if (self.MoveDown(currentStones, oppStones, i, j) != None):
                        n = Node(self.MoveDown(currentStones, oppStones, i, j), oppStones, not oppTurn, depth + 1, self.alpha, self.beta, depthLimit=self.depthLimit)
                        if (self.ShouldPrune(n)):
                            return moves
                        else:
                            moves.append(n)

                    if (self.MoveUpLeft(currentStones, oppStones, i, j) != None):
                        n = Node(self.MoveUpLeft(currentStones, oppStones, i, j), oppStones, not oppTurn, depth + 1, self.alpha, self.beta, depthLimit=self.depthLimit)
                        if (self.ShouldPrune(n)):
                            return moves
                        else:
                            moves.append(n)

                    if (self.MoveUpRight(currentStones, oppStones, i, j) != None):
                        n = Node(self.MoveUpRight(currentStones, oppStones, i, j), oppStones, not oppTurn, depth + 1, self.alpha, self.beta, depthLimit=self.depthLimit)
                        if (self.ShouldPrune(n)):
                            return moves
                        else:
                            moves.append(n)

                    if (self.MoveDownLeft(currentStones, oppStones, i, j) != None):
                        n = Node(self.MoveDownLeft(currentStones, oppStones, i, j), oppStones, not oppTurn, depth + 1, self.alpha, self.beta, depthLimit=self.depthLimit)
                        if (self.ShouldPrune(n)):
                            return moves
                        else:
                            moves.append(n)

                    if (self.MoveDownRight(currentStones, oppStones, i, j) != None):
                        n = Node(self.MoveDownRight(currentStones, oppStones, i, j), oppStones, not oppTurn, depth + 1, self.alpha, self.beta, depthLimit=self.depthLimit)
                        if (self.ShouldPrune(n)):
                            return moves
                        else:
                            moves.append(n)
        return moves

    #get random moves
    def AllNextNodes(self, currentStones, oppStones, oppTurn: bool, depth):
        moves = []
        for i in range(0, 4):
            for j in range(0, 4):
                if (oppTurn):
                    #minimizer
                    if (currentStones[i][j] > 0 or oppStones[i][j] == 0):
                        continue
                    
                    if (self.MoveLeft(oppStones, currentStones, i, j) != None):
                        moves.append(Node(currentStones, self.MoveLeft(oppStones, currentStones, i, j), not oppTurn, depth + 1, self.alpha, self.beta, minimax=False))

                    if (self.MoveRight(oppStones, currentStones, i, j) != None):
                        moves.append(Node(currentStones, self.MoveRight(oppStones, currentStones, i, j), not oppTurn, depth + 1, self.alpha, self.beta, minimax=False))

                    if (self.MoveUp(oppStones, currentStones, i, j) != None):
                        moves.append(Node(currentStones, self.MoveUp(oppStones, currentStones, i, j), not oppTurn, depth + 1, self.alpha, self.beta, minimax=False))

                    if (self.MoveDown(oppStones, currentStones, i, j) != None):
                        moves.append(Node(currentStones, self.MoveDown(oppStones, currentStones, i, j), not oppTurn, depth + 1, self.alpha, self.beta, minimax=False))

                    if (self.MoveDownLeft(oppStones, currentStones, i, j) != None):
                        moves.append(Node(currentStones, self.MoveDownLeft(oppStones, currentStones, i, j), not oppTurn, depth + 1, self.alpha, self.beta, minimax=False))

                    if (self.MoveDownRight(oppStones, currentStones, i, j) != None):
                        moves.append(Node(currentStones, self.MoveDownRight(oppStones, currentStones, i, j), not oppTurn, depth + 1, self.alpha, self.beta, minimax=False))

                    if (self.MoveUpLeft(oppStones, currentStones, i, j) != None):
                        moves.append(Node(currentStones, self.MoveUpLeft(oppStones, currentStones, i, j), not oppTurn, depth + 1, self.alpha, self.beta, minimax=False))

                    if (self.MoveUpRight(oppStones, currentStones, i, j) != None):
                        moves.append(Node(currentStones, self.MoveUpRight(oppStones, currentStones, i, j), not oppTurn, depth + 1, self.alpha, self.beta, minimax=False))

                    
                else:
                    #maximizer
                    if (oppStones[i][j] > 0 or currentStones[i][j] == 0):
                        continue

                    if (self.MoveLeft(currentStones, oppStones, i, j) != None):
                        moves.append(Node(self.MoveLeft(currentStones, oppStones, i, j), oppStones, not oppTurn, depth + 1, self.alpha, self.beta, minimax=False))

                    if (self.MoveRight(currentStones, oppStones, i, j) != None):
                        moves.append(Node(self.MoveRight(currentStones, oppStones, i, j), oppStones, not oppTurn, depth + 1, self.alpha, self.beta, minimax=False))

                    if (self.MoveUp(currentStones, oppStones, i, j) != None):
                        moves.append(Node(self.MoveUp(currentStones, oppStones, i, j), oppStones, not oppTurn, depth + 1, self.alpha, self.beta, minimax=False))

                    if (self.MoveDown(currentStones, oppStones, i, j) != None):
                        moves.append(Node(self.MoveDown(currentStones, oppStones, i, j), oppStones, not oppTurn, depth + 1, self.alpha, self.beta, minimax=False))

                    if (self.MoveUpLeft(currentStones, oppStones, i, j) != None):
                        moves.append(Node(self.MoveUpLeft(currentStones, oppStones, i, j), oppStones, not oppTurn, depth + 1, self.alpha, self.beta, minimax=False))

                    if (self.MoveUpRight(currentStones, oppStones, i, j) != None):
                        moves.append(Node(self.MoveUpRight(currentStones, oppStones, i, j), oppStones, not oppTurn, depth + 1, self.alpha, self.beta, minimax=False))

                    if (self.MoveDownLeft(currentStones, oppStones, i, j) != None):
                        moves.append(Node(self.MoveDownLeft(currentStones, oppStones, i, j), oppStones, not oppTurn, depth + 1, self.alpha, self.beta, minimax=False))

                    if (self.MoveDownRight(currentStones, oppStones, i, j) != None):
                        moves.append(Node(self.MoveDownRight(currentStones, oppStones, i, j), oppStones, not oppTurn, depth + 1, self.alpha, self.beta, minimax=False))
        return moves
    
    def ShouldPrune(self, n):
        if (not self.oppTurn):
            if (n.evalation > self.alpha):
                self.alpha = n.evalation
                if self.depth == 1:
                    self.bestNextMove = n.currConfig
            if (n.beta < self.alpha):
                self.alpha = n.beta
                if self.depth == 1:
                    self.bestNextMove = n.currConfig
        else:
            if (n.evalation < self.beta):
                self.beta = n.evalation
            if (n.alpha > self.beta):
                self.beta = n.alpha

        return (self.alpha >= self.beta)



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
            
    def MoveUpLeft(self, currentStones, oppStones, i, j):
        if i != 0 and j!=0:
            stones = currentStones[i][j]
            move = copy.deepcopy(currentStones)
            increment = 1
            while oppStones[i-increment][j-increment] == 0 and j-increment > 0 and i-increment > 0 and stones > 0:
                if (increment < stones):
                    move[i-increment][j-increment] += increment
                    stones-=increment
                else:
                    #rest of stones
                    move[i-increment][j-increment] += stones
                    stones = 0
                increment+=1

            if (move != currentStones or (increment == 1 and oppStones[i-increment][j-increment] == 0)):
                move[i - increment + (oppStones[i-increment][j-increment] != 0)][j - increment + (oppStones[i-increment][j-increment] != 0)] += stones
                move[i][j] = 0
                return move
            
    def MoveUpRight(self, currentStones, oppStones, i, j):
        if i!= 0 and j != 3:
            stones = currentStones[i][j]
            move = copy.deepcopy(currentStones)
            increment = 1
            while oppStones[i-increment][j+increment] == 0 and j+increment < 3 and i-increment > 0 and stones > 0:
                if (increment < stones):
                    move[i-increment][j+increment] += increment
                    stones-=increment
                else:
                    #rest of stones
                    move[i-increment][j+increment] += stones
                    stones = 0
                increment+=1

            if (move != currentStones or (increment == 1 and oppStones[i-increment][j+increment] == 0)):
                move[i - increment + (oppStones[i-increment][j+increment] != 0)][j + increment - (oppStones[i-increment][j+increment] != 0)] += stones
                move[i][j] = 0
                return move
            
    def MoveDownLeft(self, currentStones, oppStones, i, j):
        if i != 3 and j != 0:
            stones = currentStones[i][j]
            move = copy.deepcopy(currentStones)
            increment = 1
            while oppStones[i+increment][j-increment] == 0 and  i+increment < 3 and j-increment > 0 and stones > 0:
                if (increment < stones):
                    move[i+increment][j-increment] += increment
                    stones-=increment
                else:
                    #rest of stones
                    move[i+increment][j-increment] += stones
                    stones = 0
                increment+=1

            if (move != currentStones or (increment == 1 and oppStones[i+increment][j-increment] == 0)):
                move[i + increment - (oppStones[i+increment][j-increment] != 0)][j - increment + (oppStones[i+increment][j-increment] != 0)] += stones
                move[i][j] = 0
                return move
            
    def MoveDownRight(self, currentStones, oppStones, i, j):
        if i != 3 and j != 3:
            stones = currentStones[i][j]
            move = copy.deepcopy(currentStones)
            increment = 1
            while oppStones[i+increment][j+increment] == 0 and i+increment < 3 and j+increment < 3 and stones > 0:
                if (increment < stones):
                    move[i+increment][j+increment] += increment
                    stones-=increment
                else:
                    #rest of stones
                    move[i+increment][j+increment] += stones
                    stones = 0
                increment+=1

            if (move != currentStones or (increment == 1 and oppStones[i+increment][j+increment] == 0)):
                move[i + increment - (oppStones[i+increment][j+increment] != 0)][j + increment - (oppStones[i+increment][j+increment] != 0)] += stones
                move[i][j] = 0
                return move

    def EvaluationFunction(self):
        #Idea 1: How many moves do I have left
        # e = 0

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
        #                 if (self.MoveUpLeft(self.currConfig, self.opponentConfig, i, j) != None):
        #                     e+=1
        #                 if (self.MoveUpRight(self.currConfig, self.opponentConfig, i, j) != None):
        #                     e+=1
        #                 if (self.MoveDownLeft(self.currConfig, self.opponentConfig, i, j) != None):
        #                     e+=1
        #                 if (self.MoveDownRight(self.currConfig, self.opponentConfig, i, j) != None):
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
        #                 if (self.MoveUpLeft(self.opponentConfig, self.currConfig, i, j) != None):
        #                     e-=1
        #                 if (self.MoveUpRight(self.opponentConfig, self.currConfig, i, j) != None):
        #                     e-=1
        #                 if (self.MoveDownLeft(self.opponentConfig, self.currConfig, i, j) != None):
        #                     e-=1
        #                 if (self.MoveDownRight(self.opponentConfig, self.currConfig, i, j) != None):
        #                     e-=1
        # return e
    
        #Idea 2: How many spaces do I take up
        # e=0

        # for i in range(0, 4):
        #     for j in range(0, 4):
        #         if (self.currConfig[i][j] > 0):
        #             e+=1
        #         elif(self.opponentConfig[i][j] > 0):
        #             e-=1

        # return e

        # #Idea 3: # of white moves - # of blacks moves

        # curNode = Node(self.currConfig, self.opponentConfig, oppTurn=False, depth=1, minimax = False)
        # oppNode = Node(self.opponentConfig, self.currConfig, oppTurn=False, depth=1, minimax = False)
        # return len(curNode.nextNodes) - len(oppNode.nextNodes)


        # #Idea 4: a mix approach
        curNode = Node(self.currConfig, self.opponentConfig, oppTurn=False, depth=1, minimax = False)
        oppNode = Node(self.opponentConfig, self.currConfig, oppTurn=False, depth=1, minimax = False)

        white = 0
        black = 0

        for i in range(0, 4):
            for j in range(0, 4):
                if (self.currConfig[i][j] > 0):
                    white += 1
                elif (self.opponentConfig[i][j] > 0):
                    #to help favour higher stacks for black
                    black += self.opponentConfig[i][j]
                else:
                    for node in oppNode.nextNodes:
                        if node.currConfig[i][j] > 0:
                            black += 1
                            break
                    
                    for node in curNode.nextNodes:
                        if node.currConfig[i][j] > 0:
                            white += 1
                            break

        return white - 3*black

    




class Player:
    def __init__(self, isWhite = True):
        self.stones = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        if (isWhite):
            self.stones[0][0] = 10
        else:
            self.stones[3][3] = 10

            
    # given possbile next move, get all terminal values
    def miniMaxMove(self, otherPlayer, turns):
        if (turns>20 and turns<30):
           curNode = Node(self.stones, otherPlayer.stones, False, 1, depthLimit=4)
        elif(turns>=30 and turns<40):
           curNode = Node(self.stones, otherPlayer.stones, False, 1, depthLimit=5)
        else:
           curNode = Node(self.stones, otherPlayer.stones, False, 1, depthLimit=3)
        
        self.stones = curNode.bestNextMove

    #random move
    def randomMove(self, otherPlayer):
        curNode = Node(self.stones, otherPlayer.stones, False, 1, minimax = False)
        if (len(curNode.nextNodes) != 0):
            ranNode = random.choice(curNode.nextNodes)
            self.stones = ranNode.currConfig
    
    #has lost
    def hasLost(self, otherPlayer):
        curNode = Node(self.stones, otherPlayer.stones, False, 1, minimax = False)
        return len(curNode.nextNodes) == 0

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
white = Player()

n = 1
whiteMove = True
while(not black.hasLost(white) and not white.hasLost(black) and n<40):
    print("turn " + str(n))
    n+=1

    if (whiteMove):
        white.miniMaxMove(black, n)
    else:
        black.randomMove(white)

    printBoard(white.stones, black.stones)
    print("\n")
    whiteMove = not whiteMove

if(n>=40):
    print("terminated as it took too long")
else:
    if (black.hasLost(white)):
        print("white wins")
    else:
        print("black wins")




