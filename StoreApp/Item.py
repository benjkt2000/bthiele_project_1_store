from DAO import *

class Item():
    def __init__(self, item_id: int, item_name: int, price: float, current_inventory: int):
        self.item_id = item_id
        self.item_name = item_name
        self.price = price
        self.current_inventory = current_inventory

    def print_item_details(self):
        print("item id: ", self.item_id)
        print("item name: ", self.item_name)
        print("price: ", self.price)
        print("in stock: ", self.current_inventory)
        print("")

    def get_id(self):
        return self.item_id

    def get_item_name(self):
        return self.item_name

    def get_price(self):
        return self.price

    def get_current_inventory(self):
        return self.current_inventory

    def update_item(self, new_inventory: int):
         self.current_inventory = new_inventory
         update_item_in_inventory(self.item_id, new_inventory)

