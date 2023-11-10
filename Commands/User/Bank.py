from Commands.Enter import Enter
from Commands.Registrar import Registrar
from Commands.User.Client import Client


class Bank:
    registrar: Registrar
    client: Client
    enter: Enter
    banks = []

    def __init__(self, enter, client):
        while len(self.banks) <= self.client.get_ID():
            self.banks.append(0)
        self.client = client
        self.enter = enter

    def make_accounts(self):
        self.banks.insert(self.client.ID, 1000)

    def deduct_from_bank(self, payment):
        ID = self.client.get_ID()
        if self.registrar.proceed_with_order():
            new_bank_total = self.banks.pop(ID) - payment
            if new_bank_total < 0:
                print("Invalid Payment")
            elif new_bank_total >= 0:
                print("****************************************************************************")
                for name in self.enter.client_list:
                    if ID == self.enter.client.get_ID():
                        print(self.enter.client.get_name() + "'s new bank balance: $" + new_bank_total)
                        break
                print("****************************************************************************")
