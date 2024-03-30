#Enum options for the attribute exhibition location
from enum import Enum
class Exhibition_location(Enum):
    permanent_galleries = 1
    exhibition_halls = 2
    outdoor_spaces = 3

class MuseumItem:
    '''A parent class to store important details about museum items (the attributes are protected to allow inheritance)'''

    #constructor
    def __init__(self, title = '', artist = '', date_of_creation = '', historical_significance = '',
                 exhibition_location = Exhibition_location.permanent_galleries):

        self._title = title                                         #title of the museum item
        self._artist = artist                                       #the name of the artist
        self._date_of_creation = date_of_creation                   #year of creation
        self._historical_significance = historical_significance     #description of the historical importance of the item
        self._exhibition_location = exhibition_location              #the location of the event


    #setter and getter functions
    def set_title(self, title):
       self._title = title

    def get_title(self):
        return self._title

    def set_artist(self, artist):
        self._artist = artist

    def get_artist(self):
        return self._artist

    def set_date_of_creation(self, date):
        self._date_of_creation = date

    def get_date_of_creation(self):
        return self._date_of_creation

    def set_historical_significance(self, his_sign):
        self._historical_significance = his_sign

    def get_historical_significance(self):
        return self._historical_significance

    def set_exhibition_location(self, location):
        self._exhibition_location = location

    def get_exhibition_location(self):
        return self._exhibition_location



    #a function to return the catalog with the important attributes
    def display_catalog(self):
        return (f"Title: {self._title}\n"
                f"Artist: {self._artist}\n"
                f"Date Of Creation: {self._date_of_creation}\n"
                f"Historical Significance: {self._historical_significance}\n"
                f"Exhibition Location: {self._exhibition_location.name}")



