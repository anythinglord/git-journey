from random import randint
from util import get_name
import time

class Citizen:
    def __init__(self):
        self.name = get_name()
        self.age = 0
        self.maxAge = randint(60, 80)
        self.school = ''

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def setSchool(self, school):
        self.school = school
    
    def sickness(self, level):
        return randint(0, 5 - level)

    def simulate(self):
        print('Max age: ', self.maxAge)
        for age in range(self.maxAge):
            if age == 5: print(self.name, 'entry in the school..')
            if age == 16: print(self.name, 'exit of the school..')
            time.sleep(0.05)