import numpy as np
import random


INITALTEMP = 100
ALPHA = 1


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

def SA():
    CurrentSolution = RandomSolution()
    BestSolution = CurrentSolution

    temp = INITALTEMP

    while (temp > 0.05):
        for _ in range(300):
            NewSolution = Neightbourhood(CurrentSolution)
            DeltaCost = NewSolution.cost - CurrentSolution.cost
            
            if (DeltaCost > 0):
                CurrentSolution = NewSolution
            else:
                x = random.random()
                if (x < np.exp(-DeltaCost/temp)):
                    CurrentSolution = NewSolution

            if CurrentSolution.cost < BestSolution.cost:
                BestSolution = CurrentSolution

        #linear
        temp -= ALPHA

        #Geo
        # temp *= ALPHA

        #Slow
        # temp = temp/(1 + (BETA*temp))

    return BestSolution

bestSolution= SA()
print("best solution is (" + str(bestSolution.x1) + " ," +  str(bestSolution.x2) + ")")
print("best cost is " + str(bestSolution.cost))

