passenger_name = "Aarav"
destination = "Goa"
ticket_price = 850.50
number_of_tickets = 3
is_available = True

morning_ticket_price = 700
evening_ticket_price = 900


print("Passenger Name:", passenger_name)
print("Destination:", destination)
print("Ticket Price:", ticket_price)
print("Number of Tickets:", number_of_tickets)
print("Tickets Available:", is_available)
print("Morning Ticket Price:", morning_ticket_price)
print("Evening Ticket Price:", evening_ticket_price)


total_cost = ticket_price * number_of_tickets
print("Total Cost:", total_cost)


morning_ticket_price, evening_ticket_price = evening_ticket_price, morning_ticket_price
print("After swapping:")
print("Morning Ticket Price:", morning_ticket_price)
print("Evening Ticket Price:", evening_ticket_price)