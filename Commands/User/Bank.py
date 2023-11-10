from Commands.Enter import Enter
from Commands.Registrar import Registrar
from Commands.User.Client import Client


class Bank:
    registrar: Registrar
    client: Client
    enter: Enter
    banks = []

    def __init__(self, enter, client):
        while len(self.banks) <= len(enter.client_list):
            self.banks.append(0)
        self.client =  client
        self.enter = enter

    def make_accounts(self):
        self.banks.insert(self.client.ID, 1000)


    def deduct_from_bank(self, payment):
        ID = self.client.get_ID()