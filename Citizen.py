from random import randint
from util import get_name

class Citizen:
    def __init__(self):
        self.name = get_name()
        self.age = randint(20, 80)

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age