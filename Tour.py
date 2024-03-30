from Event import Event
class Tour(Event):
    '''A child class derived from the parent class Event'''

    #constructor
    def __init__(self, event_name = '', event_date = '', event_location = '', event_duration = '', guide_name = '', group_size = 0):
        super().__init__(event_name, event_date, event_location, event_duration)             #calling the parent class's constructor for inheritance
        self.__guide_name = guide_name                      #responsible employee for guiding visitor
        self.__group_size = group_size                      #the number of visitors in a group

    #setter and getter
    def set_guide_name(self, guide_name):
        self.__guide_name = guide_name

    def get_guide_name(self):
        return self.__guide_name

    def set_group_size(self, group_size):
        self.__group_size = group_size

    def get_group_size(self):
        return self.__group_size

    #a function to print information related to the tour
    def display_tour(self):
        event_method = super().display_event()
        extra = f", Guide Name: {self.__guide_name}, Group Size: {self.__group_size}"
        return event_method + extra

