class Account():
    def __init__(self, user_id: int, username: str, password: str, first_name: str, last_name: str, admin_status: bool):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.admin_status = admin_status

    