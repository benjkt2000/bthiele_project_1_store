from DAO import *
from Views import *


def main():
    # Create database if one does not exist
    create_database()

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

 




