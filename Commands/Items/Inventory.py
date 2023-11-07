from Commands.Items.Book import Book
from Commands.Items.CD import CD
from Commands.Items.DVD import DVD


class Inventory:
    in_stock = [Book("Narnia", True, 15.99, 0, 300), Book("LOTR", True, 5000, 1, 10000),
                Book("Animal Farm", True, 1.99, 2, 250), Book("The Iliad", True, 40.25, 3, 800),
                Book("The Bible", True, 1500000, 4, 999999), CD("Thriller", True, 8.95, 5, 250),
                CD("Hotel California", True, 6.95, 6, 100), CD("Back in Black", True, 2.99, 7, 150),
                CD("The Planets", True, 150.75, 8, 50000), CD("Ride of the Valkyries", True, 250.25, 9, 250),
                DVD("Star Wars", True, 8.95, 10, 600), DVD("Hotel California", True, 10.55, 11, 550),
                DVD("Back in Black", True, 10.75, 12, 1000), DVD("The Planets", True, 25.25, 13, 1025),
                DVD("Ride of the Valkyries", True, 12.25, 14, 1202)]

    def inventory_value(self, in_stock):
        total = 0
        for items in in_stock:
            total += self.in_stock.pop(items)
        return total

    def init_items(self, in_stock):
        self.avail_items(self.in_stock)
        print("Total cost of inventory: ")
        print(f"$ {self.inventory_value(self.in_stock)}")

    def handle_restock(self, in_stock):
        print("Sold products: ")
        self.sold_items(self.in_stock)
        sold_prod_ID = input("Select a product type to restock (select by ID): ")
        for items in in_stock:
            if self.in_stock[items].ID == sold_prod_ID:
                print(f"Restocked: {self.in_stock[items].itemName}")
                self.in_stock[items].status = True

    def add_item(self, in_stock, item_type, item_amount):
        if item_type == 1:
            while item_amount > 0:
                item_price = input("CD price? ")
                item_ID = input("CD ID? ")
                item_length = input("CD Length? ")
                item_name = input("CD Name? ")
                self.in_stock.append(CD(item_name, True, item_price, item_ID, item_length))
                item_amount -= 1
        elif item_type == 2:
            while item_amount > 0:
                item_price = input("Book price? ")
                item_ID = input("Book ID? ")
                item_length = input("Book Length? ")
                item_name = input("Book Name? ")
                self.in_stock.append(Book(item_name, True, item_price, item_ID, item_length))
                item_amount -= 1
        elif item_type == 3:
            while item_amount > 0:
                item_price = input("DVD price? ")
                item_ID = input("DVD ID? ")
                item_length = input("DVD Length? ")
                item_name = input("DVD Name? ")
                self.in_stock.append(Book(item_name, True, item_price, item_ID, item_length))
                item_amount -= 1
        print("Current Inventory")
        self.avail_items(self.in_stock)

    def avail_items(self, in_stock):
        for items in in_stock:
            if isinstance(self.in_stock[items], CD) and self.in_stock[items].status:
                self.init_items(self.in_stock[items])
            elif isinstance(self.in_stock[items], Book) and self.in_stock[items].status:
                self.init_items(self.in_stock[items])
            elif isinstance(self.in_stock[items], DVD) and self.in_stock[items].status:
                self.init_items(self.in_stock[items])

    def sold_items(self, in_stock):
        for item in in_stock:
            if not self.in_stock[item].status:
                print("Name: ", self.in_stock[item].itemName,
                      "\nPrice: ", self.in_stock[item].price,
                      "\nID: ", self.in_stock[item].ID)
                if isinstance(self.in_stock[item], CD):
                    print("\nCD Length: ", self.in_stock[item].cd_length)
                elif isinstance(self.in_stock[item], Book):
                    print("\nPage Count: ", self.in_stock[item].pages)
                elif isinstance(self.in_stock[item], DVD):
                    print("\nDVD Length: ", self.in_stock[item].dvd_length)

    def compare_items(self, in_stock):
        self.avail_items(self.in_stock)
        id_1, id_2 = input("Select two items by ID to compare: ").split()
        compare_items = []
        for items in in_stock:
            for item in in_stock:
                if item.ID == id_1 or item.ID == id_2:  # Simplify the condition
                    print("Name: ", item.itemName)
                    compare_items.append(self.instantiate_item(item))

    @staticmethod
    def instantiate_item(item):
        return item.__class__(
            item.itemName,
            True,
            item.price,
            item.ID,
            None
        )

    def sell_item(self, ID, in_stock):
        for items in in_stock:
            if self.in_stock[items].ID == ID:
                print("Sold: ", self.in_stock[items].itemName)
                self.in_stock[items].status = False

    def refund_all_items(self, in_stock):
        for items in in_stock:
            if not self.in_stock[items].status:
                self.in_stock[items].status = True
