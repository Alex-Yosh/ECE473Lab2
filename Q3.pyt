import random
import csv

#Read csvs
DistanceMatrix= []
with open("./asignment-2-Distance.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    for i in range(0, len(row)):
        row[i] = int(row[i])
    DistanceMatrix.append(row)


FlowMatrix= []
with open("./assignment-2-Flow.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    for i in range(0, len(row)):
        row[i] = int(row[i])
    FlowMatrix.append(row)


TABUSIZE = 5
NUMOFLOCATIONS = 20
NUMONEIGHBOURSCHOOSEN = 10
MAXITERATIONS = 1000

def CalculateCost(solution):
    TotalDistance = 0
    TotalFlow = 0
    for i in range(NUMOFLOCATIONS):
        #cost = flow * distance
        if (i == NUMOFLOCATIONS-1):
            TotalDistance += DistanceMatrix[solution[-1]][solution[0]]
            TotalFlow += FlowMatrix[-1][0]
            # print(str(DistanceMatrix[solution[-1]][solution[0]]) + " " + str(FlowMatrix[-1][0]))
        else:
            TotalDistance += DistanceMatrix[solution[i]][solution[i + 1]]
            TotalFlow += FlowMatrix[i][i + 1]
            # print(str(DistanceMatrix[solution[i]][solution[i + 1]]) + " " + str(FlowMatrix[i][i + 1]))
    return TotalFlow * TotalDistance

def CreateRandomInitialSolution():
    #create list from 1 -> 20
    solution = list(range(NUMOFLOCATIONS))
    #shuffle list
    random.shuffle(solution)
    return solution

# x = [2, 0, 1, 11, 12, 17, 16, 15, 10, 5, 6, 7, 8, 13, 18, 19, 14, 9, 4, 3]
# print(x)
# print(CalculateCost(x))


def GetNeighborhood(solution):
    neighbors = []

    for i in range(NUMOFLOCATIONS):
        for j in range(i + 1, len(solution)):
            neighbor = solution[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)

    # use less then entire neighbourhood
    return random.sample(neighbors, NUMONEIGHBOURSCHOOSEN)

def TabuSearch():
    #generate random solution
    CurrentSolution = CreateRandomInitialSolution()
    CurrentCost = CalculateCost(CurrentSolution)

    BestSolution = CurrentSolution[:]
    BestCost = CurrentCost

    tabu_list = []
    
    #start looping
    for i in range(MAXITERATIONS):
        neighbors = GetNeighborhood(BestSolution)
        
        # sort in order of cost
        neighbors.sort(key=CalculateCost)
        
        
        for n in neighbors:
            if n not in tabu_list:
            #asipration condition
            # or (n in tabu_list and CalculateCost(n) < BestCost):
                CurrentSolution = n
                break
        
        CurrentCost = CalculateCost(CurrentSolution)

        if CurrentCost < BestCost:
            BestSolution = CurrentSolution[:]
            BestCost = CurrentCost

        if len(tabu_list) >= TABUSIZE:
            tabu_list.pop(0) 

        tabu_list.append(CurrentSolution)

    return BestSolution, BestCost

solution, cost = TabuSearch()

print(solution)
print(cost)