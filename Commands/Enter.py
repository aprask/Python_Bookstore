from Commands.User.Client import Client


class Enter:
    client: Client
    client_list = []
    payment_types = []

    def __init__(self, client):
        self.client = client
        self.client_list.append(client)
        self.payment_types.append(client.payment_method)

    @staticmethod
    def party_size(self):
        return len(self.client_list)

    def list_customers(self):
        for client in self.client_list:
            print(client.name)

    def can_purchase(self, purchaser_id):
        for client in self.client_list:
            if client.ID == purchaser_id:
                return True
        return False

    def get_client(self):
        return self.client

    def set_client(self, changed_client):
        self.client = changed_client

    def get_customer_payments(self):
        return self.payment_types
