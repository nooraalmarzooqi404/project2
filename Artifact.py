from MuseumItem import MuseumItem, Exhibition_location

class Artifact(MuseumItem):
    '''A child class derived from MuseumItem class'''

    #Constructor
    def __init__(self, title = '', artist = '', date_of_creation = '', historical_significance = '',
                 exhibition_location = Exhibition_location.permanent_galleries, material = '', discovery_location = ''):
        super().__init__(title, artist, date_of_creation, historical_significance,exhibition_location )      #calling the constructor of the parent class
        self.__material = material
        self.__discovery_location = discovery_location

    #setter and getter functions 
    def set_material(self, material):
        self.__material = material

    def get_material(self):
        return self.__material

    def set_discovery_location(self, location):
        self.__discovery_location = location

    def get_discovery_locaation(self):
        return self.__discovery_location
    #a function to print a catalog of the artifact
    def display_catalog(self):
        MuseumItem_catalog = super().display_catalog()  # calling the method from the parent class
        extra = f"\nMaterial: {self.__material}\nDiscovery Location: {self.__discovery_location}"
        return MuseumItem_catalog + extra

