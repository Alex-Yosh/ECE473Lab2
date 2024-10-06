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

    # use less then entire neighbourhood. 210 total - 110
    return random.sample(neighbors, len(neighbors)-110)

def TabuSearch(TabuListSize):
    #generate random solution
    CurrentSolution = CreateRandomInitialSolution()
    CurrentCost = CalculateCost(CurrentSolution)

    BestSolution = CurrentSolution[:]
    BestCost = CurrentCost

    tabu_list = []
    
    interationsWithoutnewBest = 0

    #start looping
    for l in range(MAXITERATIONS):

        neighbors = GetNeighborhood(BestSolution)
        
        # sort in order of cost
        neighbors.sort(key=CalculateCost)

        #experiment 5
        if (interationsWithoutnewBest >= 10):
            tabu_list = []
        
        foundSolution = False
        for i in range(NUMOFLOCATIONS):
            for j in range(i + 1, NUMOFLOCATIONS):
                for n in neighbors:
                    if (n[i], n[j]) not in tabu_list or ((n[i], n[j]) in tabu_list and CalculateCost(n) < BestCost):
                        #asipration condition
                        # or (n in tabu_list and CalculateCost(n) < BestCost):
                        CurrentSolution = n
                        foundSolution = True
                        tabu_list.append((n[i], n[j]))
                        break
                if (foundSolution):
                    break
            if (foundSolution):
                    break

        CurrentCost = CalculateCost(CurrentSolution)

        if CurrentCost < BestCost:
            BestSolution = CurrentSolution[:]
            BestCost = CurrentCost
            interationsWithoutnewBest = 0
        else:
            interationsWithoutnewBest += 1

        if len(tabu_list) >= TabuListSize:
            tabu_list.pop(0) 


    return BestSolution, BestCost


# for j in range(10):
# dynamicTabuSize = random.randint(1, 20)
SumCost = 0
for i in range(20):
    # solution, cost = TabuSearch(dynamicTabuSize)
    solution, cost = TabuSearch(TABUSIZE)
    # print(solution)
    # print(cost)
    SumCost += cost
print("Tabu size is " + str(TABUSIZE))
print("average cost is " + str(float(SumCost)/20))
print("\n")