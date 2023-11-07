from Commands.Registrar import Registrar


class Client:
    name: str
    ID = 0
    order_status: bool
    premium: bool
    payment_method: str
    register: Registrar

    def __init__(self, name, member_type, payment_type):
        self.name = name
        self.premium = member_type
        self.payment_method = payment_type
        self.ID += 1

    def display_member_type(self):
        if self.premium:
            return 'premium member'
        else:
            return 'standard member'


