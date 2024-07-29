# Login Menu
from Util import *
import re
import logging

def execute_login_menu():
    command = -1
    while command != 3:
        print('LOGIN MENU')
        print('1. Login')
        print('2. Create Account')
        command = input('Please enter a command: ')
        print("")
        if command == '1':
            return login()
        elif command == '2':
            return execute_create_user_menu()
        else:
            print('Invalid Command.\n')

def login():
    valid_credentials = False
    while valid_credentials != True:
        print('LOGIN MENU')
        username = input('Username?: ')
        password = input('Password?: ')

        valid_credentials = validate_credentials(username, password, retrieve_all_users())
        if valid_credentials == False:
            print('Invalid username or password. Please try again.\n')
        else: 
            print('Login Success!\n')
            logging.info(f'User \'{username}\' logged in. ')
            return retrieve_user_from_database(username)
        
def execute_create_user_menu():
    valid_username = False
    new_username = ''
    while valid_username == False:         
        new_username = input('Please Enter a new username: ')
         
        if check_if_user_exists_by_username(new_username.strip(), retrieve_all_users()):
            print("Username already taken. Please try again.\n")
        else:
            print("Valid Username")
            valid_username = True
    new_password = input('Please enter a password: ')
    new_first_name = input('Please Enter a new first name: ')
    new_last_name = input('Please Enter a new last name: ')

    add_account(new_username, new_password, new_first_name, new_last_name)
    print('Account Successfuly Created.\n')
    logging.info(f'New User \'{new_username}\' created. ')
    return retrieve_user_from_database(new_username)


# User Menu

def execute_user_menu(account: Account):
    current_account = account
    command = -1
    while command != 5:
        print('USER MENU')
        print('1. Browse Items')
        print('2. View Cart')
        print('3. View Transaction History')
        print('4. Modify Account Information')
        print('5. Exit Application')
        
        command = input('Please enter a command: ')
        print("")

        if command == '1':
            execute_browse_items_menu(current_account)
        elif command == '2':
            execute_view_cart_menu(current_account)
        elif command == '3':
            current_account.list_of_transactions =  current_account.get_account_transactions(current_account.user_id)
            current_account.view_all_transactions()
            logging.info(f'User \'{current_account.username}\' displayed all his/her transactions.')
        elif command == '4':
            execute_modify_account_info_menu(current_account)
        elif command == '5':
            return False        
        else:
            print('Invalid Command.\n')

def execute_browse_items_menu(account: Account):
    current_account = account
    command = -1
    while command != 3:
        print('BROWSE ITEMS')
        print('1. Display Items')
        print('2. Add Item To Cart')
        print('3. Return To Previous Menu')
        
        command = input('Please enter a command: ')
        print("")

        if command == '1':
            display_items(get_list_of_items())
            logging.info(f'User \'{current_account.username}\' displayed all items. ')
        
        elif command == '2':
            item_id = 0
            item_already_exists = True
            while item_already_exists == True:
                item_id = input('Please enter an item id: ')
                if item_id.isdigit():
                    if current_account.shopping_cart.check_if_item_is_in_cart(int(item_id)):
                        print('Item already exists in cart. Please use VIEW CART menu to update.\n')
                    elif check_if_item_exists(int(item_id), get_list_of_items()) == False:
                        print('Item does not exist in database.\n') 
                    else:
                        item_already_exists = False
                else:
                    print('Input must be an integer.\n')

            vaild_quantity = False
            quantity = 0
            while vaild_quantity == False:
                quantity = input('Please enter a quantity: ')
                if quantity.isdigit():
                    vaild_quantity = True
                else:
                    print('Input must be an integer.\n')

            success = current_account.shopping_cart.add_item_to_cart(int(item_id), int(quantity))

            if(success):
                print('Item successfuly added to cart.\n')
                logging.info(f'User \'{current_account.username}\' added an item. ')
                current_account.shopping_cart.show_cart()
            else:
                print('Failed to add item to cart\n')
            

        elif command == '3':
            return None     
        else:
            print('Invalid Command.\n')

def execute_view_cart_menu(account: Account):
    current_account = account
    command = -1
    while command != 5:
        print('CART MENU')
        print('1. Show Current Cart')
        print('2. Update/Remove Item')
        print('3. Remove All Items')
        print('4. Checkout')
        print('5. Return to Previous Menu')
        
        command = input('Please enter a command: ')
        print("")

        if command == '1':
            current_account.shopping_cart.show_cart()
            logging.info(f'User \'{current_account.username}\' displayed all items in cart. ') 
       
        elif command == '2':
            if not current_account.shopping_cart.user_cart:
                print('Cart is empty.\n')
            else:
                item_id = 0
                item_already_exists = False
                while item_already_exists == False:
                    
                    item_id = input('Please enter an item id: ')
                    if item_id.isdigit():
                        if current_account.shopping_cart.check_if_item_is_in_cart(int(item_id)) == False:
                            print('Item does not exist in cart. Please use BROWSE ITEMS menu to update.\n')
                        else:
                            item_already_exists = True
                    else:
                        print('Input must be an integer.\n')
                
                vaild_quantity = False
                quantity = 0
                while vaild_quantity == False:
                    quantity = input('Please enter a quantity: ')
                    if quantity.isdigit():
                        vaild_quantity = True
                    else:
                        print('Input must be an integer.\n')

                success = current_account.shopping_cart.update_item_quantity(int(item_id), int(quantity))

                if(success):
                    print('Successfuly updated item in cart.\n')
                    logging.info(f'User \'{current_account.username}\' updated an item in his/her cart. ')
                    current_account.shopping_cart.show_cart()
                else:
                    print('Failed to update item in cart\n')
        
        elif command == '3':
            current_account.shopping_cart.clear_cart()
            print('All items have been removed from cart!\n')
            logging.info(f'User \'{current_account.username}\' cleared his/her cart. ')
        elif command == '4':
            if not current_account.shopping_cart.user_cart:
                print('Cart is empty.\n')
            else:    
                current_account.shopping_cart.checkout_items()
                print('Items have been purchased!\n')
                logging.info(f'User \'{current_account.username}\' performed cart checkout. ')
        elif command == '5':
            return None     
        else:
            print('Invalid Command.\n')

def execute_modify_account_info_menu(account: Account):
    current_account = account
    command = -1
    while command != 6:
        print('EDIT ACCOUNT')
        print('1. Show Current Information')
        print('2. Update Username')
        print('3. Update Password')
        print('4. Update First Name')
        print('5. Update Last Name')
        print('6. Return to Previous Menu')
        
        command = input('Please enter a command: ')
        print("")

        if command == '1':
            current_account.show_account_info()
            logging.info(f'User \'{current_account.username}\' displayed his/her account information. ')
        
        elif command == '2':
            valid_username = False
            new_username = ''
            while valid_username == False:         
                new_username = input('Please Enter a new username: ')
                
                if check_if_user_exists_by_username(new_username.strip(), retrieve_all_users()):
                    print("Username already taken. Please try again.")
                else:
                    print("Valid Username\n")
                    current_account.change_username(new_username)
                    valid_username = True

            print('Username Updated.\n')
            logging.info(f'User \'{current_account.username}\' updated his/her username. ')
            current_account.show_account_info()

        
        elif command == '3':
            new_password = input('Please Enter a new password: ')
            current_account.change_password(new_password)
            print('Password Changed.\n')
            logging.info(f'User \'{current_account.username}\' updated his/her password. ')
            current_account.show_account_info()

        elif command == '4':
            new_first_name = input('Please Enter a new first name: ')
            current_account.change_first_name(new_first_name)
            print('First Name Changed.\n')
            logging.info(f'User \'{current_account.username}\' updated his/her first name. ')
            current_account.show_account_info()
        
        elif command == '5':
            new_last_name = input('Please Enter a new last name: ')
            current_account.change_last_name(new_last_name)
            print('Last Name Changed.\n')
            logging.info(f'User \'{current_account.username}\' updated his/her last name. ')
            current_account.show_account_info()

        elif command == '6':
            return None

        else:
            print('Invalid Command.\n')
            current_account.show_account_info()


# Admin Menu
def execute_admin_menu(account: Account):
    admin_account = account
    command = -1
    while command != 5:
        print('ADMIN MENU')
        print('1. Modify User')
        print('2. View Inventory')
        print('3. View All Transactions')
        print('4. Modify Account Information')
        print('5. Exit Application')
        
        command = input('Please enter a command: ')
        print("")

        if command == '1':
            execute_admin_modify_account_info_menu(admin_account)
        elif command == '2':
            execute_modify_items_menu(admin_account)
        elif command == '3':
            display_all_transactions(get_list_of_items())
            logging.info(f'User \'{admin_account.username}\' displayed all transactions.')
        elif command == '4':
            execute_modify_account_info_menu(admin_account)
        elif command == '5':
            return None
        else:
            print('Invalid Command.\n')


def execute_admin_modify_account_info_menu(account):
    admin_account = account
    list_of_users = retrieve_all_users()
    display_all_users(list_of_users)

    valid_id = False
    curr_user_id = 0
    while valid_id == False:
        curr_user_id = input('Please enter a user id to edit: ')
        if curr_user_id.isdigit():
            if check_if_user_exists_by_id(int(curr_user_id), list_of_users):
                print('Valid User.\n')
                valid_id = True
            else:
                print('User does not exist. Please Try again\n')
        else:
            print('Input must be an integer.\n')

    current_account = list_of_users[int(curr_user_id)]


    command = -1
    while command != 7:
        print('EDIT USER ACCOUNT')
        print('1. Show Current Information')
        print('2. Update Username')
        print('3. Update Password')
        print('4. Update First Name')
        print('5. Update Last Name')
        print('6. Grant/Revoke Admin Status')
        print('7. Return to Previous Menu')
        
        command = input('Please enter a command: ')
        print("")

        if command == '1':
            current_account.show_account_info()
            logging.info(f'User \'{admin_account.username}\' retrieved \'{current_account.username}\'s information.')
        
        elif command == '2':
            valid_username = False
            new_username = ''
            while valid_username == False:         
                new_username = input('Please Enter a new username: ')
                
                if check_if_user_exists_by_username(new_username.strip(), retrieve_all_users()):
                    print("Username already taken. Please try again.")
                else:
                    print("Valid Username\n")
                    current_account.change_username(new_username)
                    valid_username = True

            print('Username Updated.\n')
            logging.info(f'User \'{admin_account.username}\' changed \'{current_account.username}\'s username.')
            current_account.show_account_info()

        
        elif command == '3':
            new_password = input('Please Enter a new password: ')
            current_account.change_password(new_password)
            print('Password Changed.\n')
            logging.info(f'User \'{admin_account.username}\' changed \'{current_account.username}\'s password.')
            current_account.show_account_info()

        elif command == '4':
            new_first_name = input('Please Enter a new first name: ')
            current_account.change_first_name(new_first_name)
            print('First Name Changed.\n')
            logging.info(f'User \'{admin_account.username}\' changed \'{current_account.username}\'s first name.')
            current_account.show_account_info()
        
        elif command == '5':
            new_last_name = input('Please Enter a new last name: ')
            current_account.change_last_name(new_last_name)
            print('Last Name Changed.\n')
            logging.info(f'User \'{admin_account.username}\' changed \'{current_account.username}\'s last name.')
            current_account.show_account_info()

        elif command == '6':
            new_admin_status = input('Please Enter a new admin status (1 for Admin, 0 for User): ')

            if(new_admin_status.strip() == '1' or new_admin_status.strip() == '0'):
                if new_admin_status == '1':
                    current_account.change_admin_status(True)
                else:
                    current_account.change_admin_status(False)
                print('Admin status changed.\n')
                logging.info(f'User \'{admin_account.username}\' changed \'{current_account.username}\'s admin status.')
            else: 
                print('Invalid Input\n')

        elif command == '7':
            return None

        else:
            print('Invalid Command.\n')
            current_account.show_account_info()

def execute_modify_items_menu(account):
    admin_account = account
    list_of_items = get_list_of_items()
    logging.info(f'User \'{admin_account.username}\' retrived all items.')
    
    command = -1
    while command != 5:
        print('MODIFY ITEMS')
        print('1. Display Items')
        print('2. Add Item To Database')
        print('3. Remove Item From Database')
        print('4. Update Item Quantity In Database')
        print('5. Return To Previous Menu')
        
        command = input('Please enter a command: ')
        print("")

        if command == '1':
            display_items(list_of_items)
            logging.info(f'User \'{admin_account.username}\' retrived all items.')
        
        elif command == '2':
            item_id = 0
            item_already_exists = True
            while item_already_exists == True:
                item_id = input('Please enter an item id: ')
                if item_id.isdigit():
                    if check_if_item_exists(int(item_id), list_of_items):
                        print('Item already exists in database.')
                    else:
                        item_already_exists = False
                else:
                    print('Input must be an integer.')
            name = input('Please enter an item name: ')
            
            price = 0.00
            invalid_price = True
            while invalid_price == True:
                price = input('Please enter a price: ')
                if re.match(r'^-?\d+(?:\.\d+)$', price) is not None:
                    invalid_price = False
                else:
                    print('Price must be in decimal format!\n')
  
            vaild_quantity = False
            quantity = 0
            while vaild_quantity == False:
                quantity = input('Please enter a quantity: ')
                if quantity.isdigit():
                    vaild_quantity = True
                else:
                    print('Input must be an integer.\n')

            success = add_item(int(item_id), name,round(float(price), 2), int(quantity), list_of_items)

            if(success):
                print('Item successfuly added to database.\n')
                logging.info(f'User \'{admin_account.username}\' added \'{name}\' to the database.')
            else:
                print('Failed to add item to database.\n')

        elif command == '3':
            item_id = 0
            item_exists = False
            while item_exists == False:
                item_id = input('Please enter an item id: ')
                if item_id.isdigit():
                    if check_if_item_exists(int(item_id), list_of_items):
                     item_exists = True
                    else:
                        print('Item does not exist in database.\n')
                else:
                    print('Input must be an integer.\n')

            remove_item(int(item_id), list_of_items)
            print('Item has been removed from inventory.\n')
            logging.info(f'User \'{admin_account.username}\' removed item_id: \'{item_id}\' from the database.')

        elif command == '4':
            item_id = 0
            item_exists = False
            while item_exists == False:
                item_id = input('Please enter an item id: ')
                if item_id.isdigit():
                    if check_if_item_exists(int(item_id), list_of_items):
                     item_exists = True
                    else:
                        print('Item does not exist in database.\n')
                else:
                    print('Input must be an integer.\n')
            
            vaild_quantity = False
            quantity = 0
            while vaild_quantity == False:
                quantity = input('Please enter a quantity: ')
                if quantity.isdigit():
                    vaild_quantity = True
                else:
                    print('Input must be an integer.\n')

            success = update_item_quantity(int(item_id), int(quantity), list_of_items)

            if success == True:
                print('Item updated successfuly.\n')
                logging.info(f'User \'{admin_account.username}\' updated item_id: \'{item_id}\' in the database.')
            else:
                print('Item could not be updated. Quantity must be greater than current inventory.\n')

        elif command == '5':
            return None

        else:
            print('Invalid Command.\n')