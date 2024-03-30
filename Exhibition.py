from Event import Event
from MuseumItem import Exhibition_location

class Exhibition(Event):
    '''A child class derived from Event'''

    #constructor
    def __init__(self,event_name = '', event_date = '', event_location = Exhibition_location.exhibition_halls, event_duration = '', theme = '', artwork_num = 0, artifact_num = 0):
        super().__init__(event_name, event_date, event_location, event_duration)
        self.__theme = theme                                       #the theme of the exhibition
        self.__artwork_num = artwork_num                           #the number of artworks taking part in the exhibition
        self.__artifact_num = artifact_num                         #the number of artifacts taking part in the exhibition

    #setter and getter

    def set_theme(self, theme):
        self.__theme = theme

    def get_theme(self):
        return self.__theme

    def set_artwork_num(self, artwork_num):
        self.__artwork_num = artwork_num

    def get_artwork_num(self):
        return self.__artwork_num

    def set_artifact_num(self, artifact_num):
        self.__artifact_num = artifact_num

    def get_artifact_num(self):
        return self.__artifact_num

    #a function to print important details about the exhibition
    def display_exhibitoin(self):
        Event_method = super().display_event()
        extra = f", Theme: {self.__theme}, Number of Artworks: {self.__artwork_num}, Number of Artifacts: {self.__artifact_num}"
        return Event_method + extra


