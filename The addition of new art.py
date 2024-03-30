from MuseumItem import MuseumItem, Exhibition_location
from Artwork import Artwork
from Artifact import Artifact

#creating an object and printing the catalog
print("Adding a new artwork")
artwork1 = Artwork('The Water Lily Pond', 'Claude Monet', '1899',"A key example of Monet's dedication to capturing the French countryside, part of his series on water lilies.", Exhibition_location.outdoor_spaces, 'Oil on canvas', (93, 73))
print(artwork1.display_catalog())



print("")
#creating an object and printing the catalog
print("Adding a new artifact")
artifact1 = Artifact('Bust of Queen Nefertiti', 'Thutmose', '1345 BC', 'One of the most copied works of ancient Egypt, symbolizing the countrys art and history.', Exhibition_location.exhibition_halls, 'Limestone, stucco','Amarna, Egypt')
print(artifact1.display_catalog())
print("")

#testsing setter and getter functions
#setter and getter testing
print("Setter and getter testing:")
print(artwork1.get_artist())
artwork1.set_artist('Artist2')
print(artwork1.get_artist())

print("")

print(artifact1.get_historical_significance())
artifact1.set_material('bronze')
print(artifact1.get_material())
