from abc import ABC, abstractmethod

from Commands.Items import Inventory


class Item(ABC):
    itemName: str
    status: bool
    ID: int
    price: float
    inventory: Inventory

    def __init__(self, itemName, status, price, ID):
        self.itemName = itemName
        self.status = status
        self.price = price
        self.ID = ID

    def get_name(self):
        return self.itemName

    def set_name(self, name):
        self.itemName = name

    def get_ID(self):
        return self.ID

    def is_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def compare_to_item(self, item):
        return self.price > item.price

    def item_details(self):
        return "Item Name: " + self.itemName + "\nItem Price: " + str(self.price)

    def use_item(self):
        return "You can now use " + self.itemName

    def equals_object(self, object):
        return self == object
