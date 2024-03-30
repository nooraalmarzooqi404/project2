from MuseumItem import MuseumItem, Exhibition_location

class Artwork(MuseumItem):
    '''A child class derived from (MuseumItem) to store details about artwork'''

    #constructor
    def __init__(self, title = '', artist = '', date_of_creation = '', historical_significance = '',
                 exhibition_location = Exhibition_location.permanent_galleries, painting_type = '', frame_size = ()):
        super().__init__(title, artist, date_of_creation, historical_significance, exhibition_location)
        self.__painting_type = painting_type
        self.__frame_size = frame_size

    #setter and getter
    def set_painting_type(self, painting):
        self.__painting_type = painting

    def get_painting_type(self):
        return self.__painting_type

    def set_frame_size(self, frame):
        self.__frame_size = frame

    def get_frame_size(self):
        return self.__frame_size

    def display_catalog(self):
        MuseumItem_catalog = super().display_catalog()      #calling the method from the parent class
        extra = f" \nPainting Type: {self.__painting_type}\nFrame Size: {self.__frame_size}\n"
        return MuseumItem_catalog + extra

