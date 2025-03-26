from Citizen import Citizen
from random import randint

class Town:
    def __init__(self, name):
        self.name = name
        self.population = randint(5, 15)
        self.citizens = [Citizen() for x in range(self.population)]

    def getName(self):
        return self.name
    
    def getPopulation(self):
        return self.population