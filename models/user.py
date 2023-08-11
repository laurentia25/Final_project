from db.CRUD.users_CRUD import UsersDb


class User:
    def __init__(
            self,
            email,
            password,
            username=None,
            user_id=None,
            confirm_password=None
    ):
        self.email = email
        self.password = password
        self.username = username
        self.user_id = user_id
        self.confirm_password = confirm_password

        self.user_db = UsersDb()

    def check_in_db(self):
        users = self.user_db.read(email=self.email)
        if not users:
            raise Exception("Nu sunteți înregistrat cu acest email!")
        user = users[0]
        if user["password"] != self.password:
            raise Exception("Parolă invalidă!")
        return True
