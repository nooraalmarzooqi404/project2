#enum options for the attribute category in Visitor class
from enum import Enum

class Visitor_category(Enum):
    Adult = 1
    Child = 2
    Teacher = 3
    Student = 4
    Senior = 5

class Visitor:
    '''A class to enable users to input visitors' information and categorize them as child, adult, studnet...'''

    #constructor
    def __init__(self):
        self.__visitor_name = self.input_name("Enter visitor's name: ")
        self.__age = self.input_age("Enter visitor's age")
        self.__teacher = self.input_boolean("Is the visitor a teacher? (yes/no)")
        self.__student = self.input_boolean("Is the visitor a student? (yes/no)")
        self.__visitor_category = self.determine_category()
        self.__tickets_history = []  # This attribute holds the history of purchased tickets

    #adding the ticket to tickets history
    def add_ticket_to_history(self, ticket):
        self.__tickets_history.append(ticket)

    #a method to display the history of purchased tickets
    def display_tickets_history(self):
        from Ticket import Ticket
        for ticket in self.__tickets_history:
            ticket.print_receipt()

    #input validation for the name
    def input_name(self, prompt):
        while True:
            try:
                #this line captures the string that the user types in response to the prompt
                value = input(prompt)
                #if the input is an empty string, raise a ValueError
                if not value:
                    raise ValueError("Input cannot be empty")
                return value
            #informing the user by printing this message
            except ValueError as e:
                print(f" Invalid input: {e}")

    #input validation for the age
    def input_age(self, prompt):
        #loop until we receive a valid input
        while True:
            try:
                #converting the string input to an integer
                age = int(input(prompt))

                #giving a valid range for the age
                assert 0 < age < 120, "Age must be from 1 to 119"
                return age
            #if the input cannot be converted to an integer
            except ValueError:
                print("Please enter a valid integer for the age")
            #the age does not satisfy the assertion condition
            except AssertionError as e:
                print(e)

    #to check if the visitor is either a student or teacher or none
    def input_boolean(self, prompt):
        while True:
            try:
                #prompt the user for input
                #.strip() removes any leading and trailing whitespace (including spaces, tabs, newlines).
                #.lower() converts the string to lowercase.

                response = input(prompt).strip().lower()
                #checks if the input is either yes or no if not, raise an error
                if response not in ['yes', 'no']:
                    raise ValueError("Please respond with 'yes' or 'no'")
                #converting the user's text input into a boolean value
                return response == 'yes'
            #if there is an error, print the error message
            except ValueError as e:
                print(e)

    #determining the category based on age and job
    def determine_category(self):
        if self.__age < 18:
            return Visitor_category.Child
        elif self.__age > 60:
            return Visitor_category.Senior
        elif self.__teacher:
            return Visitor_category.Teacher
        elif self.__student:
            return Visitor_category.Student
        else:
            return Visitor_category.Adult

    #returning important info
    def display_visitor(self):
        return f" Name: {self.__visitor_name}\nAge: {self.__age}\nCategory: {self.__visitor_category}"
