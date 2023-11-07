from abc import ABC, abstractmethod

from Commands.Items import Inventory


class Item(ABC):
    itemName: str
    status: bool
    ID: int
    price: float
    inventory: Inventory

    @abstractmethod
    def __init__(self, itemName, status, price, ID):
        self.itemName = itemName
        self.status = status
        self.price = price
        self.ID = ID

    @abstractmethod
    def get_name(self):
        return self.itemName

    @abstractmethod
    def set_name(self, name):
        self.itemName = name

    @abstractmethod
    def get_ID(self):
        return self.ID

    @abstractmethod
    def is_status(self):
        return self.status

    @abstractmethod
    def set_status(self, status):
        self.status = status

    @abstractmethod
    def compare_to_item(self, item):
        return self.price > item.price

    @abstractmethod
    def item_details(self):
        return "Item Name: " + self.itemName + "\nItem Price: " + str(self.price)

    @abstractmethod
    def use_item(self):
        return "You can now use " + self.itemName

    @abstractmethod
    def equals_object(self, object):
        return self == object


class Book(Item):
    def get_name(self):
        pass

    def set_name(self, name):
        pass

    def get_ID(self):
        pass

    def is_status(self):
        pass

    def set_status(self, status):
        pass

    def compare_to_item(self, item):
        pass

    def item_details(self):
        pass

    def use_item(self):
        pass

    def equals_object(self, object):
        pass

    pages: int

    def __init__(self, itemName, status, price, ID, pages):
        super().__init__(itemName, status, price, ID)
        self.pages = pages


class DVD(Item):
    def get_name(self):
        pass

    def set_name(self, name):
        pass

    def get_ID(self):
        pass

    def is_status(self):
        pass

    def set_status(self, status):
        pass

    def compare_to_item(self, item):
        pass

    def item_details(self):
        pass

    def use_item(self):
        pass

    def equals_object(self, object):
        pass

    dvd_length: float

    def __init__(self, itemName, status, price, ID, dvd_length):
        super().__init__(itemName, status, price, ID)
        self.dvd_length = dvd_length


class CD(Item):
    def get_name(self):
        pass

    def set_name(self, name):
        pass

    def get_ID(self):
        pass

    def is_status(self):
        pass

    def set_status(self, status):
        pass

    def compare_to_item(self, item):
        pass

    def item_details(self):
        pass

    def use_item(self):
        pass

    def equals_object(self, object):
        pass

    cd_length: float

    def __init__(self, itemName, status, price, ID, cd_length):
        super().__init__(itemName, status, price, ID)
        self.cd_length = cd_length
