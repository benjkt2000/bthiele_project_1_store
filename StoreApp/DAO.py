from pymongo import MongoClient
from mock_info import *

# retrieve list of items
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

def add_transaction(transaction: dict):
    client = MongoClient()

    try:
        db = client.get_database("groceryStore")
    
        db.transactions.insert_one(transaction)

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

def update_item_quantity(item_id: int, quantity: int):
    client = MongoClient()

    try:
        db = client.get_database("groceryStore")
        
        my_query = {"item_id": item_id}
        new_values = {"$set": {"current_inventory": quantity}}
    
        db.items.update_one(my_query, new_values)

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

        db.accounts.insert_many(new_accounts)
        db.items.insert_many(new_items)

        return True

    except Exception as e:
        print("A database exception occurred:", e)


########################################################################################






