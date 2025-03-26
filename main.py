
class Town:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

print("Town v0.0.1")
town = Town("xant")
print(town.getName())