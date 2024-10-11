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


TABUSIZE = 10
NUMOFLOCATIONS = 20
NUMONEIGHBOURSCHOOSEN = 10
MAXITERATIONS = 1000

def CalculateCost(solution):
    cost = 0
    for i in range(NUMOFLOCATIONS):
        for j in range(NUMOFLOCATIONS):
            cost += FlowMatrix[i][j] * DistanceMatrix[solution[i]][solution[j]]
    return cost

def CreateRandomInitialSolution():
    #create list from 1 -> 20
    solution = list(range(NUMOFLOCATIONS))
    #shuffle list
    random.shuffle(solution)
    return solution



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

        
        foundSolution = False
        for i in range(NUMOFLOCATIONS):
            for j in range(i + 1, NUMOFLOCATIONS):
                for n in neighbors:
                    if (n[i], n[j]) not in tabu_list:
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


def TabuSearchExp3():
    #generate random solution
    CurrentSolution = CreateRandomInitialSolution()
    CurrentCost = CalculateCost(CurrentSolution)

    BestSolution = CurrentSolution[:]
    BestCost = CurrentCost

    tabu_list = []

    TabuListSize = random.randint(1, 20)
    iterationsTilSwitch = random.randint(5, 30)

    #start looping
    for l in range(MAXITERATIONS):

        iterationsTilSwitch -=1


        if (iterationsTilSwitch == 0):
            TabuListSize = random.randint(1, 20)
            iterationsTilSwitch = random.randint(5, 30)


        neighbors = GetNeighborhood(BestSolution)
        
        # sort in order of cost
        neighbors.sort(key=CalculateCost)

        
        foundSolution = False
        for i in range(NUMOFLOCATIONS):
            for j in range(i + 1, NUMOFLOCATIONS):
                for n in neighbors:
                    if (n[i], n[j]) not in tabu_list or ((n[i], n[j]) in tabu_list and CalculateCost(n) < BestCost):
                        #asipration condition
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

def TabuSearchExp4(TabuListSize):
    #generate random solution
    CurrentSolution = CreateRandomInitialSolution()
    CurrentCost = CalculateCost(CurrentSolution)

    BestSolution = CurrentSolution[:]
    BestCost = CurrentCost

    tabu_list = []

    #start looping
    for l in range(MAXITERATIONS):

        neighbors = GetNeighborhood(BestSolution)
        
        # sort in order of cost
        neighbors.sort(key=CalculateCost)

        
        foundSolution = False
        for i in range(NUMOFLOCATIONS):
            for j in range(i + 1, NUMOFLOCATIONS):
                for n in neighbors:
                    if (n[i], n[j]) not in tabu_list or ((n[i], n[j]) in tabu_list and CalculateCost(n) < BestCost):
                        #asipration condition
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


def TabuSearchExp5(TabuListSize):
    #generate random solution
    CurrentSolution = CreateRandomInitialSolution()
    CurrentCost = CalculateCost(CurrentSolution)

    BestSolution = CurrentSolution[:]
    BestCost = CurrentCost

    OverallBestSolution = []

    tabu_list = []
    
    interationsWithoutnewBest = 0

    #start looping
    for l in range(MAXITERATIONS):
        #experiment 5
        if (interationsWithoutnewBest >= 10):
            if OverallBestSolution ==[] or BestCost < CalculateCost(OverallBestSolution):
                OverallBestSolution = BestSolution
            
            #restart search
            CurrentSolution = CreateRandomInitialSolution()
            CurrentCost = CalculateCost(CurrentSolution)

            BestSolution = CurrentSolution[:]
            BestCost = CurrentCost


        neighbors = GetNeighborhood(BestSolution)
        
        # sort in order of cost
        neighbors.sort(key=CalculateCost)

        
        foundSolution = False
        for i in range(NUMOFLOCATIONS):
            for j in range(i + 1, NUMOFLOCATIONS):
                for n in neighbors:
                    if (n[i], n[j]) not in tabu_list or ((n[i], n[j]) in tabu_list and CalculateCost(n) < BestCost):
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


    return OverallBestSolution, CalculateCost(OverallBestSolution)



#exp 1
print("exp 1 \n")
SumCost = 0
s = ""
for i in range(20):
    solution, cost = TabuSearch(TABUSIZE)
    SumCost += cost
    s += str(cost) + ", "
print("Tabu size is " + str(TABUSIZE))
print(s)
print("average cost is " + str(float(SumCost)/20))
print("\n")

#exp 2
print("exp 2 \n")
SumCost = 0
size = 1
s = ""
for i in range(20):
    solution, cost = TabuSearch(size)
    SumCost += cost
    s += str(cost) + ", "
print("Tabu size is " + str(size))
print(s)
print("average cost is " + str(float(SumCost)/20))


SumCost = 0
size = 5
s = ""
for i in range(20):
    solution, cost = TabuSearch(size)
    SumCost += cost
    s += str(cost) + ", "
print("Tabu size is " + str(size))
print(s)
print("average cost is " + str(float(SumCost)/20))


SumCost = 0
size = 15
s = ""
for i in range(20):
    solution, cost = TabuSearch(size)
    SumCost += cost
    s += str(cost) + ", "
print("Tabu size is " + str(size))
print(s)
print("average cost is " + str(float(SumCost)/20))


SumCost = 0
size = 20
s = ""
for i in range(20):
    solution, cost = TabuSearch(size)
    SumCost += cost
    s += str(cost) + ", "
print("Tabu size is " + str(size))
print(s)
print("average cost is " + str(float(SumCost)/20))

print("\n")

# #exp 3
print("exp 3 \n")
SumCost = 0
s = ""
for i in range(20):
    solution, cost = TabuSearchExp3()
    SumCost += cost
    s += str(cost) + ", "
print("Tabu size is Dynamic")
print(s)
print("average cost is " + str(float(SumCost)/20))
print("\n")

# #exp 4
print("exp 4 \n")
SumCost = 0
s = ""
for i in range(20):
    solution, cost = TabuSearchExp4(TABUSIZE)
    SumCost += cost
    s += str(cost) + ", "
print("Tabu size is " + str(TABUSIZE))
print(s)
print("average cost is " + str(float(SumCost)/20))
print("\n")

# #exp 5
print("exp 5 \n")
SumCost = 0
s = ""
for i in range(20):
    solution, cost = TabuSearchExp5(TABUSIZE)
    SumCost += cost
    s += str(cost) + ", "
print("Tabu size is " + str(TABUSIZE))
print(s)
print("average cost is " + str(float(SumCost)/20))
print("\n")

