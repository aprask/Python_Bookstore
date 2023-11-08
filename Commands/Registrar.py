from Commands import Enter
from Commands.User import Client
from Commands.User import Bank


class Registrar:
    order_total: float
    enter: Enter
    customer_line = []
    line_total: int
    client: Client

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

    def handle_bank(self, payment, client):
        bank: Bank(Registrar.enter, Registrar.client)
