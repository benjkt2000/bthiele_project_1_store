from DAO import *
from Views import *
import logging


def main():
    # Initate Logging
    logging.basicConfig(filename="./StoreApp/groceryStore.log",format='%(asctime)s %(message)s')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Create database if one does not exist
    created_database = create_database()

    if created_database == True:
        logging.info('Created Database groceryStore.')
    

    # Start Menus
    run_app = True
    while run_app:
        # Execute login menu
        current_user = execute_login_menu()

        if current_user.admin_status == True:
            print(f'Logged in as {current_user.username}\n')
            run_app = execute_admin_menu(current_user)
        else:
            print(f'Logged in as {current_user.username}\n')
            run_app = execute_user_menu(current_user)

if __name__ == '__main__':
    main()

 




