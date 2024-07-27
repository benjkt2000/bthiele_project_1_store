from pymongo import MongoClient
from Mock_info import *

# Item Table Related Functions
def retrieve_all_items(): 
    client = MongoClient()

    try:
        db = client.get_database("groceryStore")

        collection_items = db.items

        items = collection_items.find()

        list_of_items = []

        for item in items:
            list_of_items.append(item)

        return list_of_items

    
    except Exception as e:
        print("A database exception occurred:", e)

def add_item_to_inventory(item_id: int, item_name: str, price: float, current_inventory: int):
    client = MongoClient()

    try:
        db = client.get_database("groceryStore")
        
        my_query = {"item_id": item_id, "item_name": item_name, "price": price, "current_inventory": current_inventory}

        db.items.insert_one(my_query)

    except Exception as e:
        print("A database exception occurred:", e)

def delete_item_from_inventory(item_id: int):
    client = MongoClient()

    try:
        db = client.get_database("groceryStore")
        
        my_query = {"item_id": item_id}

        db.items.delete_one(my_query)

    except Exception as e:
        print("A database exception occurred:", e)

def update_item_in_inventory(item_id: int, quantity: int):
    client = MongoClient()

    try:
        db = client.get_database("groceryStore")
        
        my_query = {"item_id": item_id}
        new_values = {"$set": {"current_inventory": quantity}}
    
        db.items.update_one(my_query, new_values)

    except Exception as e:
        print("A database exception occurred:", e)

# Account Table Related Functions
def find_max_account_id():
    client = MongoClient()

    try:
        db = client.get_database("groceryStore")
        
        my_query = [{"$group":{"_id": None, "maxField": {"$max": "$user_id"}}}]
    
        result = db.accounts.aggregate(my_query)

        max_user_id = 0

        for i in result:
            max_user_id = i

        return max_user_id['maxField']
            
    
    except Exception as e:
        print("A database exception occurred:", e)

def get_all_user_accounts_from_database():
    client = MongoClient()

    try:
        db = client.get_database("groceryStore")

        users = db.accounts.find()

        list_of_users = []

        for user in users:
            list_of_users.append(user)
        
        return list_of_users

    except Exception as e:
        print("A database exception occurred:", e)

def get_user_account_from_database(username: str):
    client = MongoClient()

    try:
        db = client.get_database("groceryStore")
        
        my_query = {"username": username}

        user = db.accounts.find_one(my_query)

        return user

    except Exception as e:
        print("A database exception occurred:", e)

def add_account_to_database(user_id: int, username: str, password: str, first_name: str, last_name: str, admin_status: bool):
    client = MongoClient()

    try:
        db = client.get_database("groceryStore")
        
        my_query = {"user_id": user_id, "username": username, "password": password, "first_name": first_name, "last_name": last_name, "current_transaction": [], "admin": False}

        db.accounts.insert_one(my_query)

    except Exception as e:
        print("A database exception occurred:", e)


def delete_account_from_database(user_id: int):
    client = MongoClient()

    try:
        db = client.get_database("groceryStore")
        
        my_query = {"user_id": user_id}

        db.accounts.delete_one(my_query)

    except Exception as e:
        print("A database exception occurred:", e)


def add_item_to_current_transaction(user_id: int, item_id: int, quantity: int):
    client = MongoClient()

    try:
        db = client.get_database("groceryStore")
        
        my_query = {"user_id": user_id}
        new_values = {"$push": {"current_transaction": {"item_id": item_id, "quantity": quantity}}}


        db.accounts.update_one(my_query, new_values)

    except Exception as e:
        print("A database exception occurred:", e)

def delete_user_cart_by_user_id(user_id: int):
    client = MongoClient()

    try:
        db = client.get_database("groceryStore")
        
        my_query = {"user_id": user_id}
        new_values = {"$unset": {"current_transaction": ""}}
    
        db.accounts.update_one(my_query, new_values)
        db.accounts.update_one({'user_id': user_id},{'$set': {'current_transaction': []}})

    except Exception as e:
        print("A database exception occurred:", e)

def update_item_in_cart_by_user_id(user_id: int, item_id: int, quantity: int):
    client = MongoClient()

    try:
        db = client.get_database("groceryStore")
        
        my_query = {"user_id": user_id, "current_transaction.item_id": item_id}
        new_values = {"$set": {"current_transaction.$.quantity": quantity}}
    
        db.accounts.update_one(my_query, new_values)

    except Exception as e:
        print("A database exception occurred:", e)

def delete_item_in_cart_by_user_id(user_id: int, item_id: int):
    client = MongoClient()

    try:
        db = client.get_database("groceryStore")
        
        my_query = {"user_id": user_id, "current_transaction.item_id": item_id}
        new_values = {"$set": {"current_transaction.$": ""}}
    
        db.accounts.update_one(my_query, new_values)

    except Exception as e:
        print("A database exception occurred:", e)

def remove_nulls_from_user_cart(user_id: int):
    client = MongoClient()

    try:
        db = client.get_database("groceryStore")
        
        my_query = {"user_id": user_id}
        new_values = {"$pull": {"current_transaction": ""}}
    
        db.accounts.update_one(my_query, new_values)

    except Exception as e:
        print("A database exception occurred:", e)

def update_username(user_id: int, new_username: str):
    client = MongoClient()

    try:
        db = client.get_database("groceryStore")
        
        my_query = {"user_id": user_id}
        new_values = {"$set": {"username": new_username}}
    
        db.accounts.update_one(my_query, new_values)

    except Exception as e:
        print("A database exception occurred:", e)

def update_first_name(user_id: int, new_first_name: str):
    client = MongoClient()

    try:
        db = client.get_database("groceryStore")
        
        my_query = {"user_id": user_id}
        new_values = {"$set": {"first_name": new_first_name}}
    
        db.accounts.update_one(my_query, new_values)

    except Exception as e:
        print("A database exception occurred:", e)

def update_last_name(user_id: int, new_last_name: str):
    client = MongoClient()

    try:
        db = client.get_database("groceryStore")
        
        my_query = {"user_id": user_id}
        new_values = {"$set": {"last_name": new_last_name}}
    
        db.accounts.update_one(my_query, new_values)

    except Exception as e:
        print("A database exception occurred:", e)

def update_password(user_id: int, new_password: str):
    client = MongoClient()

    try:
        db = client.get_database("groceryStore")
        
        my_query = {"user_id": user_id}
        new_values = {"$set": {"password": new_password}}
    
        db.accounts.update_one(my_query, new_values)

    except Exception as e:
        print("A database exception occurred:", e)


def update_admin_status(user_id: int, new_admin_status: bool):
    client = MongoClient()

    try:
        db = client.get_database("groceryStore")
        
        my_query = {"user_id": user_id}
        new_values = {"$set": {"admin": new_admin_status}}
    
        db.accounts.update_one(my_query, new_values)

    except Exception as e:
        print("A database exception occurred:", e)

# User Transaction Related Functions
def find_max_transaction_id():
    client = MongoClient()

    try:
        db = client.get_database("groceryStore")
        
        my_query = [{"$group":{"_id": None, "maxField": {"$max": "$transaction_id"}}}]
    
        result = db.transactions.aggregate(my_query)

        max_trans_id = 0

        for i in result:
            max_trans_id = i

        return max_trans_id['maxField']
            
    
    except Exception as e:
        print("A database exception occurred:", e)


def get_transactions_by_user_id(user_id: int):
    client = MongoClient()

    try:
        db = client.get_database("groceryStore")
        
        my_query = {"user_id": user_id}
    
        raw_user_transactions = db.transactions.find(my_query)

        user_transactions = []

        for trans in raw_user_transactions:
            user_transactions.append(trans)
       
        return user_transactions

    except Exception as e:
        print("A database exception occurred:", e)

def get_all_transactions():
    client = MongoClient()

    try:
        db = client.get_database("groceryStore")
    
        raw_user_transactions = db.transactions.find()

        user_transactions = []

        for trans in raw_user_transactions:
            user_transactions.append(trans)
       
        return user_transactions

    except Exception as e:
        print("A database exception occurred:", e)

def add_transaction(transaction: dict):
    client = MongoClient()

    try:
        db = client.get_database("groceryStore")
    
        db.transactions.insert_one(transaction)

    except Exception as e:
        print("A database exception occurred:", e)

# Database Creation
def create_database():
    client = MongoClient()

    try:
        dblist = client.list_database_names()
        
        if "groceryStore" in dblist:
            return False
        
        db = client["groceryStore"]

        new_accounts = mock_accounts 
        new_items = mock_items
        new_transaction = mock_transaction

        db.accounts.insert_many(new_accounts)
        db.items.insert_many(new_items)
        db.transactions.insert_one(new_transaction)

        return True

    except Exception as e:
        print("A database exception occurred:", e)