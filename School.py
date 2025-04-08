from util import get_name
from random import randint

class School:
    def __init__(self):
        self.name = get_name()
        self.limit = randint(0, 15)
        self.capacity = 0

    def getName(self):
        return self.name
    