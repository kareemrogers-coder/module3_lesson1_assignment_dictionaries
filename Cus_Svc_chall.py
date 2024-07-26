#Question 2

""" 2. Python Programming Challenges for Customer Service Data Handling


Objective: This assignment is designed to test and enhance your Python programming skills, focusing on real-world applications in customer service data management. You will practice correcting code, organizing customer data, and implementing a feedback system using Python dictionaries.


Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets. """

service_tickets = {
    1: {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    2: {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def next_id(): # return an ID I can use to make a new service ticket
    last_id = 0
    for id in service_tickets.keys():
        if id > last_id:
            last_id = id
    return last_id + 1

def new_ticket(): # function for creating a new ticket
    new_id = next_id()
    while True:
        customer = input("Please enter the customer name: \n")
        issue = input("Please state the issue: \n")
        print(f"Customer: {customer}, Issue: {issue}")
        correct = input("Is this information correct? (y/n): ").lower()
        if correct == 'y': # create a new ticket
            service_tickets[new_id] = {'Customer': customer, 'Issue': issue, 'Status': 'open'}
            break
        else:
            continue

def lookup():
    print(service_tickets)
    x = int(input("Please enter service ticket #: "))
    lookup_tic = service_tickets.get(x, "Not Found")
    print(lookup_tic)
    if True:
        status = input("Please Verify the issue was resolved: (y/n): ".lower())
        if status == "y":
            lookup_tic["Status"]= "closed"
            print(f"Service Ticket as been update: \n {lookup_tic}")
            # print(service_tickets)
        elif status == "n":
            print("Please continue working on service ticket")

def main():
    flag = True
    while flag:
        ans = input(''' 
-1 Open a new service ticket.
-2 Update Service ticket status.
-3 Dispay all Service ticket
-4 Quit
''')

        if ans == "1":
            new_ticket()
            continue
        elif ans == "2":
            lookup()
            continue
        elif ans == "3":
           print(f" Below is the list of ALL tickets: \n {service_tickets}")
           continue
        elif ans == "4":
            print("Exiting Service ticketing program....")
        else:
            print(" Incorrect selection please choose from the below options.")
        break

main ()