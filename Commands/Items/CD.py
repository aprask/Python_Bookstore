from Commands.Items.Item import Item
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
