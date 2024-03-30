class Event:
    '''A class to store important details about different events held by the museum'''

    #constructor
    def __init__(self, event_name = '', event_date = '', event_location = '', event_duration = ''):
        self._eventName = event_name
        self._eventDate = event_date
        self._eventLocation = event_location
        self._eventDuration = event_duration


    #setter and getter
    def set_eventName(self, event_name):
        self._eventName = event_name

    def get_eventName(self):
        return self._eventName

    def set_eventDate(self, event_date):
        self._eventDate = event_date

    def get_eventDate(self):
        return self._eventDate

    def set_eventLocation(self, event_location):
        self._eventLocation = event_location

    def get_eventLocation(self):
        return self._eventLocation

    def set_eventDuration(self, event_duration):
        self._eventDuration = event_duration

    def get_eventDuration(self):
        return self._eventDuration


    #a function to print important details about the event
    def display_event(self):
        return f"Event Name: {self._eventName}\nEvent Date: {self._eventDate}\nEvent Location: {self._eventLocation}\nEvent Duration: {self._eventDuration}"