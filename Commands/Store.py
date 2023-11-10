from Commands.Items.Inventory import Inventory
from Commands.Registrar import Registrar
from Commands.User.Admin.Admin import Admin


class Store:
    inventory: Inventory
    track_order_amount = 1
    registrar: Registrar
    item_ID_track: int
    dvd_ids = []
    cd_ids = []
    book_ids = []
    num_of_customers: int
    admin: Admin

    def open_store(self):
        open = input("Would you like to open the store? (y/n) ")
        if open.lower().__eq__('y'):
            print("Welcome! ")
            line_total = input("How many people are in line manager? ")
            self.registrar.party_total(int(line_total))
            self.num_of_customers = int(line_total) - 1

    def prep_store(self):
        if self.admin.did_pass():
            self.open_store()
        else:
            print("Failed")

    def handle_user(self):
        for i in range(len(self.registrar.get_line_total())):
            if self.registrar.enter.get_client() is None:
                break
            # call user_bank

    def user_bank(self, ID):
        if self.registrar.enter.can_purchase(ID):
            customer_name = self.registrar.handle_customer()
            print(customer_name, "'s order:\n")
            while True:
                self.item_ID_track = self.registrar.create_items(self.inventory)
                if self.item_ID_track == 5:
                    self.inventory.compare_items()
                    continue
                elif self.item_ID_track == 4:
                    print("Total Cost of Inventory: $" + self.inventory.inventory_value())


