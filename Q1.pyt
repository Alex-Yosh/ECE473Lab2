import numpy as np
import random
import matplotlib.pyplot as plt


INITALTEMP = 100
LOWTEMP = 0.05
ALPHA = 0.001


class Solution:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2
        self.cost = self.Cost()

    def Cost(self):
        return -np.cos(self.x1) * np.cos(self.x2) * np.exp(-((self.x1 - np.pi) ** 2 + (self.x2 - np.pi) ** 2))


def Neightbourhood(solution):
    x1New = 101
    x2New = 101
    while (np.abs(x1New) > 100 or np.abs(x2New) > 100):
        x1New = np.copy(solution.x1) + np.random.uniform(-5, 5)
        x2New = np.copy(solution.x2) + np.random.uniform(-5, 5)

    return Solution(x1New, x2New)

def RandomSolution():
    return Solution(np.random.uniform(-100, 100), np.random.uniform(-100, 100))

def SA(initalSolution = RandomSolution(), initalTemp = INITALTEMP, lowtemp = LOWTEMP, alpha = ALPHA):
    CurrentSolution = initalSolution
    BestSolution = CurrentSolution

    temp = initalTemp
    solutionProfile = []

    while (temp > lowtemp):
        NewSolution = Neightbourhood(CurrentSolution)
        DeltaCost = NewSolution.cost - CurrentSolution.cost
        solutionProfile.append(BestSolution.cost)
            
        if (DeltaCost > 0):
            CurrentSolution = NewSolution
        else:
            x = random.random()
            if (x < np.exp(-DeltaCost/temp)):
                CurrentSolution = NewSolution

        if CurrentSolution.cost < BestSolution.cost:
            BestSolution = CurrentSolution

        #linear
        temp -= alpha

        #Geo
        # temp *= ALPHA

        #Slow
        # temp = temp/(1 + (BETA*temp))

    return BestSolution, solutionProfile


bestSolution, _ = SA()
print("best solution is (" + str(bestSolution.x1) + ", " + str(bestSolution.x2) + ") and the cost was" + str(bestSolution.cost))


# first experiment
initalSolutions = []
results = []
for i in range(10):
    initalSolution = RandomSolution()
    initalSolutions.append(initalSolution)
    _, history = SA(initalSolution = initalSolution)
    results.append(history)

for i, history in enumerate(results):
    plt.plot(history, label=f'Initial point ({round(initalSolutions[i].x1, 2)}, {round(initalSolutions[i].x2, 2)})')
plt.title('Solution Profile vs Different Initial Points')
plt.xlabel('Iteration')
plt.ylabel('Solution Cost')
plt.legend()
plt.grid()
plt.show()

#second experiment
initalTemps = []
results = []
for i in range(10):
    initalTemp = random.randint(50, 150)
    initalTemps.append(initalTemp)
    _, history = SA(initalTemp=initalTemp)
    results.append(history)

for i, history in enumerate(results):
    plt.plot(history, label=f'Initial Temp: {initalTemps[i]}')
plt.title('Solution Profile vs Different Initial Temps')
plt.xlabel('Iteration')
plt.ylabel('Solution Cost')
plt.legend()
plt.grid()
plt.show()

#third experiment
initalAlphas = []
results = []
for i in range(10):
    alpha = random.uniform(0.0005, 0.002)
    initalAlphas.append(alpha)
    _, history = SA(alpha=alpha)
    results.append(history)

for i, history in enumerate(results):
    plt.plot(history, label=f'alpha: {round(initalAlphas[i], 4)}')
plt.title('Solution Profile vs Different Alphas')
plt.xlabel('Iteration')
plt.ylabel('Solution Cost')
plt.legend()
plt.grid()
plt.show()