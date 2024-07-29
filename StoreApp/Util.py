from DAO import *
from Item import *
from Account import *
from prettytable import PrettyTable
import os

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

def display_items(list_of_items: dict):
    t = PrettyTable(['Item ID', 'Item Name', 'Price', 'In Stock'])    


    for item in list_of_items.values():
            t.add_row([item.get_id(),item.get_item_name(), item.get_price(), item.get_current_inventory()])  

    print(t,'\n')   

def add_item(item_id: int, item_name: str, price: float, current_inventory: int, list_of_items: dict):  
    add_item_to_inventory(item_id, item_name, price, current_inventory)
    list_of_items[item_id] = Item(item_id, item_name, price, current_inventory)

    return True

def remove_item(item_id: int, list_of_items: dict):
    list_of_users = retrieve_all_users()

    for user in list_of_users.values():
        user.shopping_cart.update_item_quantity(item_id, 0)

    del list_of_items[item_id]
    delete_item_from_inventory(item_id)

    return True

def update_item_quantity(item_id: int, quantity: int, list_of_items: dict):
    if quantity >= 0 and quantity >= list_of_items[item_id].get_current_inventory():
        list_of_items[item_id].update_item(quantity)
        return True
    
    return False
     
def check_if_item_exists(item_id: int, list_of_items: dict):
    if item_id in list_of_items.keys():
        return True
    return False


# General Account Functions
def retrieve_all_users():
    raw_users = get_all_user_accounts_from_database()

    list_of_users = {}
    for user in raw_users:

        list_of_users[user['user_id']] = Account(user['user_id'], user['username'], user['password'], user['first_name'], user['last_name'], user['admin'], user['current_transaction'])

    return list_of_users

def check_if_user_exists_by_id(user_id: int, list_of_users: dict):
    if user_id in list_of_users.keys():
        return True
    
    return False

def find_largest_user_id(list_of_users: dict):
    largest_user_id = 0
    for id in list_of_users.keys():
        if largest_user_id < id:
            largest_user_id = id

    return largest_user_id 

def display_all_users(list_of_users: dict):
    t = PrettyTable(['User ID', 'First Name', 'Last Name', 'Username', 'Password', "Admin Status"])    

    for acc in list_of_users.values():
            t.add_row([acc.user_id,acc.first_name, acc.last_name, acc.username, acc.password, acc.admin_status])  

    print(t,'\n') 

def delete_account(user_id: int, list_of_users: dict):
    account = list_of_users[user_id]

    account.show_account_info()

    account.shopping_cart.clear_cart()
    delete_account_from_database(user_id)
    del list_of_users[user_id]

    display_all_users(list_of_users)
    
# Transaction Functions
def display_all_transactions(list_of_items: dict):
    list_of_transactions = get_all_transactions()
    total_profit = 0

    for trans in list_of_transactions:
        print("Transaction ID: ", trans['transaction_id'])

        date = str(trans['date'])
        date_split = date.split("T")
        print("Date:", date_split[0])
        
        print("User ID: ", trans['user_id'])

        items_list = trans['items']
        t = PrettyTable(['Item ID', 'Name', 'Price', 'Quantity'])             

        for item in items_list:
            item_obj = list_of_items[item['item_id']] 
            item_name = item_obj.get_item_name()
            price = item_obj.get_price() 
            
            t.add_row([item['item_id'], item_name, price, item['quantity']])

        print(t)
        print('Total Cost: ', trans['total_cost'], '\n')

        total_profit += trans['total_cost']

    print(f"TOTAL PROFIT: ", "{:.2f}".format(total_profit))


# Authentication Functions
def check_if_user_exists_by_username(username: str, list_of_users: dict):
    for acc in list_of_users.values():
        if username == acc.username:
            return True
    
    return False

def validate_credentials(username: str, password: str, list_of_users: dict):
    for acc in list_of_users.values():
        if username == acc.username and password == acc.password:
            return True 
    
    return False

def retrieve_user_from_database(username: str):
    raw_account = get_user_account_from_database(username)

    account = Account(raw_account['user_id'], raw_account['username'], raw_account['password'], raw_account['first_name'], raw_account['last_name'], raw_account['admin'], raw_account['current_transaction'])

    return account

def add_account(username: str, password: str, first_name: str, last_name: str):
    max_user_id = find_largest_user_id(retrieve_all_users())
    add_account_to_database(max_user_id + 1, username, password, first_name, last_name, False)
    return True





