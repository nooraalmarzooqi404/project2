from Visitor import Visitor_category
from enum import Enum
class Event_type(Enum):
    Tour = 1
    Exhibition = 2
    Special_event = 3

class Ticket:
    '''A class to store ticket-related information, calculate ticket price and print receipt'''

    general_tick_price = 63
    VAT_percentage = 0.05
    exhibition_charge = 12.0       #assumption
    tour_charge = 15.0             #assumption
    special_event_charge = 20.5    #assumption

    #constructor
    def __init__(self, visitor_name = '', visitor_category = Visitor_category.Adult, event_name = '', event_type = Event_type.Exhibition, date_of_visit = '', is_group = False):
        self.__visitor_name = visitor_name
        self.__visitor_category = visitor_category
        self.__event_name = event_name
        self.__event_type = event_type
        self.__date_of_visit = date_of_visit
        self.__is_group = is_group
        self.__ticket_price = self.calculate_price()


    #allowing visitor to purchase tickets by filling in information
    def purchase_ticket(self):
        #asking the visitor to enter some details and validate the input
        try:
            self.__visitor_name = input("Enter visitor's name: ").strip()
            if not self.__visitor_name:
                raise ValueError("Visitor's name cannot be empty.")

            self.__event_name = input("Enter event name: ").strip()
            if not self.__event_name:
                raise ValueError("Event name cannot be empty.")

            date_input = input("Enter date of visit (YYYY-MM-DD): ").strip()
            #date validation
            if not date_input:
                raise ValueError("Date of visit cannot be empty.")
            self.__date_of_visit = date_input

            event_type_input = input("Confirm event type (Tour, Exhibition, Special_event): ").strip()
            self.__event_type = Event_type[event_type_input]

            group_input = input("Is this a group purchase? (yes/no): ").strip().lower()
            self.__is_group = True if group_input == 'yes' else False

            #calculate the ticket price
            self.__ticket_price = self.calculate_price()
            print(f"Purchase is successful. Ticket price: {self.__ticket_price:.2f} AED")

        #printing error messages
        except ValueError as e:
            print(f"Error: {e}")

        except KeyError as e:
            print(f"Invalid event type entered. Please enter one of: Tour, Exhibition, Special_event.")


   #a function to calculate final ticket price
    def calculate_price(self):
        #free ticket for some visitor categories
        if self.__visitor_category in [Visitor_category.Child, Visitor_category.Senior, Visitor_category.Student, Visitor_category.Teacher]:
            return 0

        price = Ticket.general_tick_price     #starting with the original price of 63

        #price changes based on event type
        if self.__event_type == Event_type.Exhibition:
            price += Ticket.exhibition_charge

        elif self.__event_type == Event_type.Tour:
            price += Ticket.tour_charge

        else:
            price += Ticket.special_event_charge

        #50% discount for group tickets
        if self.__is_group:
            price *= 0.5

        final_price_with_VAT = price + (price * Ticket.VAT_percentage)
        return final_price_with_VAT

#a function to print the receipt

    def print_receipt(self):
        print("\n--- Ticket Purchase Receipt ---")
        print(f"Visitor Name: {self.__visitor_name}")
        print(f"Event Name: {self.__event_name}")
        print(f"Event Type: {self.__event_type.name}")
        print(f"Date of Visit: {self.__date_of_visit}")
        print(f"Group Purchase: {'Yes' if self.__is_group else 'No'}")
        print(f"Ticket Price: {self.__ticket_price:.2f} AED")
        print("--------------------------------\n")


