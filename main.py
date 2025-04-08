from Town import Town

print("Town v0.0.1")
town = Town("xant")

print('Town name: ', town.getName())
print('Town population: ', town.getPopulation())
#for i in town.citizens:
    #print('Citizen name: ', i.getName())
print(town.citizens[0].simulate())