# Login Menu
from Util import *
import re

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
            return retrieve_user_from_database(username)
        
def execute_create_user_menu():
    valid_username = False
    new_username = ''
    while valid_username == False:         
        new_username = input('Please Enter a new username: ')
         
        if check_if_user_exists_by_username(new_username.strip(), retrieve_all_users()):
            print("Username already taken. Please try again.")
        else:
            print("Valid Username")
            valid_username = True
    new_password = input('Please enter a password: ')
    new_first_name = input('Please Enter a new first name: ')
    new_last_name = input('Please Enter a new last name: ')

    add_account(new_username, new_password, new_first_name, new_last_name)
    print('Account Successfuly Created.')
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
            current_account.view_all_transactions()
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
        
        elif command == '2':
            item_id = 0
            item_already_exists = True
            while item_already_exists == True:
                item_id = input('Please enter an item id: ')
                if current_account.shopping_cart.check_if_item_is_in_cart(int(item_id)):
                    print('Item already exists in cart. Please use VIEW CART menu to update.')
                else:
                    item_already_exists = False
            
            quantity = input('Please enter a quantity: ')

            success = current_account.shopping_cart.add_item_to_cart(int(item_id), int(quantity))

            if(success):
                print('Item successfuly added to cart.')
                current_account.shopping_cart.show_cart()
            else:
                print('Failed to add item to cart')

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
       
        elif command == '2':
            item_id = 0
            item_already_exists = False
            while item_already_exists == False:
                item_id = input('Please enter an item id: ')
                if current_account.shopping_cart.check_if_item_is_in_cart(int(item_id)) == False:
                    print('Item does not exist in cart. Please use BROWSE ITEMS menu to update.')
                else:
                    item_already_exists = True
            
            quantity = input('Please enter a quantity: ')

            success = current_account.shopping_cart.update_item_quantity(int(item_id), int(quantity))

            if(success):
                print('Successfuly updated item in cart.')
                current_account.shopping_cart.show_cart()
            else:
                print('Failed to add item to cart')
        
        elif command == '3':
            current_account.shopping_cart.clear_cart()
            print('All items have been removed from cart!')
        elif command == '4':
            current_account.shopping_cart.checkout_items()
            print('Items have been purchased!')
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
            current_account.show_account_info()

        
        elif command == '3':
            new_password = input('Please Enter a new password: ')
            current_account.change_password(new_password)
            print('Password Changed.\n')
            current_account.show_account_info()

        elif command == '4':
            new_first_name = input('Please Enter a new first name: ')
            current_account.change_first_name(new_first_name)
            print('First Name Changed.\n')
            current_account.show_account_info()
        
        elif command == '5':
            new_last_name = input('Please Enter a new last name: ')
            current_account.change_last_name(new_last_name)
            print('Last Name Changed.\n')
            current_account.show_account_info()

        elif command == '6':
            return None

        else:
            print('Invalid Command.\n')
            current_account.show_account_info()


# Admin Menu
def execute_admin_menu(account: Account):
    current_account = account
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
            execute_admin_modify_account_info_menu()
        elif command == '2':
            execute_modify_items_menu()
        elif command == '3':
            display_all_transactions(get_list_of_items())
        elif command == '4':
            pass
        elif command == '5':
            return None
        else:
            print('Invalid Command.\n')


def execute_admin_modify_account_info_menu():
    list_of_users = retrieve_all_users()
    display_all_users(list_of_users)

    valid_id = False
    curr_user_id = 0
    while valid_id == False:
        curr_user_id = input('Please enter a user id to edit: ')

        if check_if_user_exists_by_id(int(curr_user_id), list_of_users):
            print('Valid User.\n')
            valid_id = True
        else:
            print('User does not exist. Please Try again')

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
            current_account.show_account_info()

        
        elif command == '3':
            new_password = input('Please Enter a new password: ')
            current_account.change_password(new_password)
            print('Password Changed.\n')
            current_account.show_account_info()

        elif command == '4':
            new_first_name = input('Please Enter a new first name: ')
            current_account.change_first_name(new_first_name)
            print('First Name Changed.\n')
            current_account.show_account_info()
        
        elif command == '5':
            new_last_name = input('Please Enter a new last name: ')
            current_account.change_last_name(new_last_name)
            print('Last Name Changed.\n')
            current_account.show_account_info()

        elif command == '6':
            new_admin_status = input('Please Enter a new admin status (1 for Admin, 0 for User): ')

            if(new_admin_status.strip() == '1' or new_admin_status.strip() == '0'):
                if new_admin_status == '1':
                    current_account.change_admin_status(True)
                else:
                    current_account.change_admin_status(False)
                print('Admin status changed.')
            else: 
                print('Invalid Input\n')

        elif command == '7':
            return None

        else:
            print('Invalid Command.\n')
            current_account.show_account_info()

def execute_modify_items_menu():
    list_of_items = get_list_of_items()
    
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
        
        elif command == '2':
            item_id = 0
            item_already_exists = True
            while item_already_exists == True:
                item_id = input('Please enter an item id: ')
                if check_if_item_exists(int(item_id), list_of_items):
                    print('Item already exists in database.')
                else:
                    item_already_exists = False
            
            name = input('Please enter an item name: ')
            
            price = 0.00
            invalid_price = True
            while invalid_price == True:
                price = input('Please enter a price: ')
                if re.match(r'^-?\d+(?:\.\d+)$', price) is not None:
                    invalid_price = False
                else:
                    print('Price must be in decimal format!\n')
  
            quantity = input('Please enter a quantity: ')

            success = add_item(int(item_id), name,float("{:.2f}".format(float(price))), int(quantity), list_of_items)

            if(success):
                print('Item successfuly added to database.\n')
            else:
                print('Failed to add item to cart\n')

        elif command == '3':
            pass

        elif command == '4':
            pass

        elif command == '5':
            return None

        else:
            print('Invalid Command.\n')