from Ticket import Ticket, Event_type
from Visitor import Visitor_category

print("Test Case  - Purchasing Tickets:")
individual_ticket = Ticket('Reem', Visitor_category.Adult, 'Red Exhibition',
                               Event_type.Exhibition, '2024-04-03')
individual_ticket.purchase_ticket()
individual_ticket.print_receipt()




'''For this test case, the user needs to enter the required details to purchase the ticket and print the reciept. 
Since the output depends on user input, the output for the test cases are explained in the pdf file'''