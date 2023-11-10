from Commands import Enter
from Commands.User import Client
from Commands.User import Bank
from Commands.User.Upgrade import Upgrade

class Registrar:
    order_total: float
    enter: Enter
    customer_line = []
    line_total: int
    client: Client
    bank: Bank
    upgrade: Upgrade

    def enter_store(self, client):
        self.enter(client)

    @staticmethod
    def is_order_done(status):
        return status

    def check_out(self):
        self.is_order_done(True)
        print("Receipt\n")
        for customers in range(self.line_total):
            print(f"${self.enter.get_customer_payments()[customers]} "
                  f"spent by {self.enter.client.get_name()[customers]}")
            print(f"Payment Method: {self.enter.client.payment_method[customers]}")
        print(f"Line order total: {self.order_total}")

    def refund_order(self):
        if self.line_total > 1:
            print("Each of your orders have been refunded")
        else:
            print("Your order has been refunded")
        print("Receipt\n")
        for customers in range(self.line_total):
            print(f"${self.enter.get_customer_payments()[customers]} "
                  f"returned to {self.enter.client.get_name()[customers]}")
            print(f"Payment Method: {self.enter.client.payment_method[customers]}")

    def add_to_total(self, payment):
        self.order_total += payment

    @staticmethod
    def proceed_with_order():
        return True

    def handle_bank(self, payment, client, enter):
        Registrar.bank(self.enter, self.client)
        Registrar.bank.deduct_from_bank(payment)
        self.enter.get_customer_payments.append(payment)
        self.add_to_total(payment)
        print("Party Order Total: $", self.order_total)
        print("****************************************************************************\n")

    def create_items(self, inventory):
        print("\n")
        inventory.avail_items()
        print("\nType \"1\" to purchase a Book")
        print("Type \"2\" to purchase a CD")
        print("Type \"3\" to purchase a DVD")
        print("Type \"4\" to display the total inventory value")
        print("Type \"5\" to compare two items")
        return input("Which product? ")

    def party_total(self, party_total):
        self.line_total = party_total
        premium = False
        i = 0
        while i < self.line_total:
            customer_num = i + 1
            customer_name = input("Name? ")
            premium_member = input("Premium Membership? (y/n)")
            if premium_member.lower().__eq__('y'):
                premium = True
            self.customer_line.append(customer_name)
            upgraded = Upgrade(self.client(customer_name, premium, None), customer_name)
            if premium:
                upgraded.make_premium()
            else:
                upgraded.make_standard()
            upgraded.display_customers()
            i += 1

    def handle_customer(self):
        if not (len(self.customer_line) == 0):
            return self.customer_line.pop()
        else:
            return None

    def get_line_total(self):
        return self.line_total
