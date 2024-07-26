from DAO import *
from Item import *
from prettytable import PrettyTable

# General Inventory Functions
def get_list_of_items():
    raw_items = retrieve_all_items()
    
    item_catalog = {}
    
    for item in raw_items:
        id = item['item_id']
        item_name = item['item_name']
        price = item['price']
        current_inventory = item['current_inventory']
        
        item_catalog[id] = Item(id, item_name, price, current_inventory)
    
    return item_catalog


def display_items(list_of_items: list):
    t = PrettyTable(['Item ID', 'Item Name', 'Price', 'In Stock'])    


    for item in list_of_items.values():
            t.add_row([item.get_id(),item.get_item_name(), item.get_price(), item.get_current_inventory()])  

    print(t,'\n')   


def add_item(item_id: int, item_name: str, price: float, current_inventory: int):  
     add_item_to_inventory(item_id, item_name, price, current_inventory)

def remove_item(item_id: int):
    
     delete_item_from_inventory(item_id)
     

# use outside add_item
def check_if_item_exists(item_id: int, list_of_items: dict):
     if item_id in list_of_items.keys():
          return True
     return False





