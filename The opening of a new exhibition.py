from Exhibition import Exhibition
from Tour import Tour
from MuseumItem import Exhibition_location

#test case: adding new exhibition
print("Exhibition test case:")
exhibition1 = Exhibition('Roses Exhibition', 'March 30. 2024', Exhibition_location.outdoor_spaces.name, '4 days', 'Roses', 19, 7 )
print(exhibition1.display_exhibitoin())

print("")
#Tour
print("Tour test case:")
tour1 = Tour('Tour around roses exhibition', 'April 1. 2024', Exhibition_location.outdoor_spaces.name, '30 mins', 'Mark Johns', 20)
print(tour1.display_tour())