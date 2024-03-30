from MuseumItem import MuseumItem, Exhibition_location

#catalog printing
item1 = MuseumItem('The Starry Night', 'Vincent van Gogh', '1889', 'One of the most recognized paintings in the history of Western culture.', Exhibition_location.exhibition_halls)
print(item1.display_catalog())

#setter and getter testing
item1.set_title('Title1')
print(item1.get_title())