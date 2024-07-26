from DAO import *
from Item import Item
from prettytable import PrettyTable
from datetime import *

class Cart():
    def __init__(self, user_id: int, user_cart: list ):
        self.user_id = user_id

        raw_items = retrieve_all_items()

        self.item_catalog = {}
        for item in raw_items:
            id = item['item_id']
            item_name = item['item_name']
            price = item['price']
            current_inventory = item['current_inventory']
            
            self.item_catalog[id] = Item(id, item_name, price, current_inventory)

        self.user_cart = user_cart

    def show_cart(self):
        t = PrettyTable(['Item ID', 'Item Name', 'Price', 'Quantity'])

        for item in self.user_cart:
            curr_item = self.item_catalog[item['item_id']] 
            name = curr_item.get_item_name()
            price = curr_item.get_price()
            quantity = item['quantity']

            t.add_row([item['item_id'], name, price, quantity])

        print(t)

    def show_item_catalog(self):
        t = PrettyTable(['Item ID', 'Item Name', 'Price', 'In Stock'])

        for item in self.item_catalog.values():
            t.add_row([item.get_id(),item.get_item_name(), item.get_price(), item.get_current_inventory()])  

        print(t)                


    def calculate_total(self):
        total_cost = 0

        for item in self.user_cart:
            curr_item = self.item_catalog[item['item_id']] 
            quantity = item['quantity']
            price = curr_item.get_price()
            total_cost += quantity * price
            
        return total_cost

    def add_item_to_cart(self, item_id: int, quantity: int):
        if item_id not in self.item_catalog.keys():
            return False
        
        if quantity <= 0:
            return False
        
        if quantity > self.item_catalog[item_id].get_current_inventory():
            return False
        
        item_object = self.item_catalog[item_id]
        item_object.update_item(item_object.get_current_inventory() - quantity)  
        cart_item = {"item_id": item_id, "quantity": quantity}
        self.user_cart.append(cart_item)
        add_item_to_current_transaction(self.user_id, item_id, quantity)

        return True
    
    def clear_cart(self):
        for item in self.user_cart:
            item_id_in_cart = item['item_id']
            user_quantity = item['quantity']

            item_in_database = self.item_catalog[item_id_in_cart] 
            item_in_database.update_item(item_in_database.get_current_inventory() + user_quantity)

        delete_user_cart_by_user_id(self.user_id)
        self.user_cart.clear()

        return True
    
    def update_item_quantity(self, item_id: int, quantity: int):
        item_exists_in_cart = False
        item_in_cart = {}
        item_in_database = None

        for item in self.user_cart:
            if item_id == item['item_id']:
                item_exists_in_cart = True
                item_in_cart = item
                item_in_database = self.item_catalog[item_id]

        if item_exists_in_cart:            
            if quantity <= 0:
                item_in_database.update_item(item_in_database.get_current_inventory() + item_in_cart['quantity'])
                delete_item_in_cart_by_user_id(self.user_id, item_id)
                remove_nulls_from_user_cart(self.user_id)
                self.user_cart.remove(item_in_cart) 
            
                return True
            
            else:
                difference = item_in_cart['quantity'] - quantity            
                if (difference + item_in_database.get_current_inventory()) >= 0:
                    item_in_database.update_item(item_in_database.get_current_inventory() + difference)
                    update_item_in_cart_by_user_id(self.user_id, item_id, quantity)
                    self.user_cart.remove(item_in_cart) 
                    item_in_cart['quantity'] = quantity
                    self.user_cart.append(item_in_cart)
            
                    return True
                
        return False
    
    def checkout_items(self):
        transaction = {}
        transaction['user_id'] = self.user_id
        dt = datetime.now()
        transaction['date'] = datetime.isoformat(dt)
        transaction['items'] = self.user_cart 
        transaction['total_cost'] = self.calculate_total()

        add_transaction(transaction)

        self.clear_cart()

        return True








user_id = 4            
    
user_cart = [{ 'item_id': 4, 'quantity': 80}]


new_cart = Cart(user_id, user_cart)

new_cart.show_item_catalog()
new_cart.show_cart()

print(new_cart.checkout_items())
# print(new_cart.add_item_to_cart(4,6))

# new_cart.show_item_catalog()
# new_cart.show_cart()

# delete_item_in_cart_by_user_id(4,0)
# remove_nulls_from_user_cart(4)


