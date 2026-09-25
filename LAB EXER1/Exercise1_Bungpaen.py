# ITEC 204 - Laboratory Exercise 1
# IT Automation Incident Ticket Manager

tickets = [
    {
        "id": "INC1392939",
        "bot": "BOT-Inventory",
        "description": "Failed to generate the daily report"
    },
    {
        "id": "INC1392940",
        "bot": "BOT-Email",
        "description": "Failed to send the scheduled notification"
    },
    {
        "id": "INC1392941",
        "bot": "BOT-DataSync",
        "description": "Encountered an error during data transfer"
    },
    {
        "id": "INC1392942",
        "bot": "BOT-Invoice",
        "description": "Failed to process an invoice"
    },
    {
        "id": "INC1392943",
        "bot": "BOT-Report",
        "description": "Failed to generate the weekly report"
    },
    {
        "id": "INC1392944",
        "bot": "BOT-FileTransfer",
        "description": "Failed to upload the required file"
    },
    {
        "id": "INC1392945",
        "bot": "BOT-DataEntry",
        "description": "Encountered an error while entering records"
    },
    {
        "id": "INC1392946",
        "bot": "BOT-Backup",
        "description": "Failed to complete the scheduled backup"
    },
    {
        "id": "INC1392947",
        "bot": "BOT-Validation",
        "description": "Failed to validate the submitted records"
    },
    {
        "id": "INC1392948",
        "bot": "BOT-Notification",
        "description": "Failed to send the system alert"
    }
]


def print_header(title):
    print("\n+======================================================+")
    print(f"|{title:^54}|")
    print("+======================================================+")


def print_message(message):
    print("+------------------------------------------------------+")
    print(f"| {message:<52} |")
    print("+------------------------------------------------------+")


def add_ticket():
    print_header("ADD INCIDENT TICKET")

    incident_id = input("\n >> Incident ID       : ")

    for ticket in tickets:
        if ticket["id"] == incident_id:
            print()
            print_message("[ERROR] Incident ID already exists!")
            return

    bot = input(" >> Bot Name          : ")
    description = input(" >> Short Description : ")

    new_ticket = {
        "id": incident_id,
        "bot": bot,
        "description": description
    }

    tickets.append(new_ticket)

    print()
    print_message("[SUCCESS] Incident ticket added successfully!")


def display_tickets():
    print("\n+==================================================================================================+")
    print("|                                      ACTIVE INCIDENT TICKETS                                     |")
    print("+===============+====================+=============================================================+")
    print("| INCIDENT ID   | BOT                | SHORT DESCRIPTION                                           |")
    print("+===============+====================+=============================================================+")

    if len(tickets) == 0:
        print("|                             NO ACTIVE INCIDENT TICKETS                                            |")
    else:
        for ticket in tickets:
            incident_id = ticket["id"]
            bot = ticket["bot"]
            description = ticket["description"]

            print(f"| {incident_id:<13} | {bot:<18} | {description:<59} |")

    print("+===============+====================+=============================================================+")


def search_ticket():
    print_header("SEARCH INCIDENT TICKET")

    incident_id = input("\n >> Enter Incident ID : ")

    for ticket in tickets:
        if ticket["id"] == incident_id:
            print("\n+------------------------------------------------------+")
            print("|                    TICKET FOUND                      |")
            print("+------------------------------------------------------+")
            print(f"| Incident ID : {ticket['id']:<38} |")
            print(f"| Bot         : {ticket['bot']:<38} |")
            print(f"| Description : {ticket['description']:<38} |")
            print("+------------------------------------------------------+")
            return

    print()
    print_message("[ERROR] Incident ticket not found!")


def remove_ticket():
    print_header("REMOVE RESOLVED TICKET")

    incident_id = input("\n >> Enter Incident ID : ")

    for ticket in tickets:
        if ticket["id"] == incident_id:
            tickets.remove(ticket)

            print()
            print_message("[SUCCESS] Resolved ticket removed!")
            return

    print()
    print_message("[ERROR] Incident ticket not found!")


def count_tickets():
    print_header("ACTIVE TICKET COUNT")

    total = len(tickets)

    print("|                                                      |")
    print(f"|              TOTAL ACTIVE TICKETS: {total:<17} |")
    print("|                                                      |")
    print("+======================================================+")


def show_menu():
    print("\n+======================================================+")
    print("|                                                      |")
    print("|       IT AUTOMATION INCIDENT TICKET MANAGER          |")
    print("|                                                      |")
    print("+======================================================+")
    print("|                                                      |")
    print("|   [1]  Add Incident Ticket                           |")
    print("|   [2]  Display Active Tickets                        |")
    print("|   [3]  Search Incident Ticket                        |")
    print("|   [4]  Remove Resolved Ticket                        |")
    print("|   [5]  Count Active Tickets                          |")
    print("|   [6]  Exit                                          |")
    print("|                                                      |")
    print("+======================================================+")
    print("|              ITEC 204 - LAB EXERCISE 1               |")
    print("+======================================================+")


while True:
    show_menu()

    choice = input("\n >> Select an option [1-6]: ")

    if choice == "1":
        add_ticket()

    elif choice == "2":
        display_tickets()

    elif choice == "3":
        search_ticket()

    elif choice == "4":
        remove_ticket()

    elif choice == "5":
        count_tickets()

    elif choice == "6":
        print("\n+======================================================+")
        print("|                PROGRAM TERMINATED                    |")
        print("|                  Thank you!                          |")
        print("+======================================================+")
        break

    else:
        print()
        print_message("[ERROR] Please select from 1 to 6!")