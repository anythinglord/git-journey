from Town import Town
from School import School

print("Town v0.0.1")
town = Town("xant")
school = School()

print('Town name: ', town.getName())
print('Town population: ', town.getPopulation())
print('School name', school.getName())
print(town.citizens[0].simulate())