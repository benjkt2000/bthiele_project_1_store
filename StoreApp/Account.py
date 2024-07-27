from DAO import *
from Cart import *
from Item import *

class Account():
    def __init__(self, user_id: int, username: str, password: str, first_name: str, last_name: str, admin_status: bool, cart: list):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.admin_status = admin_status
        self.shopping_cart = Cart(user_id, cart)
        self.list_of_transactions = get_transactions_by_user_id(user_id)

    def get_account_transactions(self, user_id):
            return get_transactions_by_user_id(user_id)
    

    def show_account_info(self):
         print('User ID: ', self.user_id)
         print('Username: ', self.username)
         print('Password: ', self.password)
         print('First Name: ', self.first_name)
         print('Last Name: ', self.last_name)
         print('Admin Status: ', self.admin_status,"\n")

    def change_username(self, new_username: str):
        update_username(self.user_id, new_username)
        self.username = new_username
  
    def change_first_name(self, new_first_name: str):
        update_first_name(self.user_id, new_first_name)
        self.first_name = new_first_name

    def change_last_name(self, new_last_name: str):
        update_last_name(self.user_id, new_last_name)
        self.last_name = new_last_name

    def change_password(self, new_password: str):
        update_password(self.user_id, new_password)
        self.password = new_password

    def change_admin_status(self, new_status: bool):
        update_admin_status(self.user_id, new_status)
        self.admin_status = new_status

    def view_all_transactions(self):
        for trans in self.list_of_transactions:
            print("Transaction ID: ", trans['transaction_id'])

            date = str(trans['date'])
            date_split = date.split("T")
            print("Date:", date_split[0])

            items_list = trans['items']
            t = PrettyTable(['Item ID', 'Name', 'Price', 'Quantity'])             

            for item in items_list:
                item_obj = self.shopping_cart.item_catalog[item['item_id']] 
                item_name = item_obj.get_item_name()
                price = item_obj.get_price() 
                
                t.add_row([item['item_id'], item_name, price, item['quantity']])

            print(t)
            print('Total Cost: ', trans['total_cost'], '\n')
        

    
