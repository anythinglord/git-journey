from Citizen import Citizen
class Town:
    def __init__(self, name):
        self.name = name
        self.citizens = [Citizen() for x in range(5)]

    def getName(self):
        return self.name

print("Town v0.0.1")
town = Town("xant")
print('Town name: ', town.getName())
for i in town.citizens:
    print('Citizen name: ', i.getName())