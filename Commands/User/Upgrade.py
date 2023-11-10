from Commands.Enter import Enter
from Commands.User.Client import Client


class Upgrade:
    client: Client
    enter: Enter
    payment: str
    name: str

    def __init__(self, client, name):
        self.client = client
        self.name = name

    def make_premium(self):
        print("Premium Membership Activated")
        self.client.set_premium_member(True)
        print("We need to verify your purchase date: ")
        self.client.payment_due_date()
        payment_type = input("How will you be paying for your purchases and membership? ")
        self.enter.client_list.append(Client(self.name, True, payment_type))

    def make_standard(self):
        print("Standard Membership Activated")
        payment_type = input("How will you be paying for your purchases and membership? ")
        self.enter.client_list.append(Client(self.name, False, payment_type))

    def display_customers(self):
        print("\nCurrent Party Members: ")
        print(self.enter.list_customers())