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

    def get_ID(self):
        return self.ID

    def set_ID(self, new_id):
        self.ID = new_id

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_payment_method(self):
        return self.payment_method

    def set_payment_method(self, new_payment):
        self.payment_method = new_payment

    def set_premium_member(self, new_premium):
        self.premium = new_premium

    @staticmethod
    def payment_due_date():
        month = input("What month did you purchase your membership? (Numbers 1-12 represent months): ")
        premium_payment = 7.55
        match month:
            case 1:
                print(f"Your membership payment of ${premium_payment} will be due in February")
            case 2:
                print(f"Your membership payment of ${premium_payment} will be due in March")
            case 3:
                print(f"Your membership payment of ${premium_payment} will be due in April")
            case 4:
                print(f"Your membership payment of ${premium_payment} will be due in May")
            case 5:
                print(f"Your membership payment of ${premium_payment} will be due in June")
            case 6:
                print(f"Your membership payment of ${premium_payment} will be due in July")
            case 7:
                print(f"Your membership payment of ${premium_payment} will be due in August")
            case 8:
                print(f"Your membership payment of ${premium_payment} will be due in September")
            case 9:
                print(f"Your membership payment of ${premium_payment} will be due in October")
            case 10:
                print(f"Your membership payment of ${premium_payment} will be due in November")
            case 11:
                print(f"Your membership payment of ${premium_payment} will be due in December")
            case 12:
                print(f"Your membership payment of ${premium_payment} will be due in January")
            case _:
                print("Error")
