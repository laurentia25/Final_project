import uuid

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

    def validate_input_request(self):
        """
        1. Verificam ca am primit toate campurile necesare pentru creare user nou.
        2. Validam username-ul -> self.validate_username()
        3. Validam parola -> self._validate_password()
        4. Verificam ca parolele introduse coincid
        """
        self.check_fields()
        self.validate_username()
        self.validate_password()
        self.check_passwords()

    def check_fields(self):
        if not self.email or not self.password or not self.username or not self.confirm_password:
            raise Exception("Nu ați completat toate câmpurile!")

    def validate_username(self):
        """
        1. Verificam ca username-ul nu contine caractere speciale
        invalid_chars = "!#$%^&*()+=`~/?<>,\\|\"\'|țșăîâÂÎȚȘĂ"
        """
        invalid_chars = "!#$%^&*()+=`~/?<>,\\|\"\'|țșăîâÂÎȚȘĂ"
        for char in self.password:
            if char in invalid_chars:
                raise Exception("Username-ul nu trebuie sa contina caractere invalide!")

    def validate_password(self):
        """
        1. Verificam ca avem lungimea de minim 8 caractere
        2. Verificam ca avem cel putin o litera mare
        3. Verificam ca avem cel putin un caracter special (-, /, ?, @ etc)
        special_chars = "!@#$%^&*()-=_+[]{}|;':\"<>,./?\\"
        """
        if len(self.password) < 8:
            raise Exception("Parola trebuie sa aibă minim 8 caractere!")
        for char in self.password:
            char.isupper()
            break
        else:
            raise Exception("Parola trebuie sa aibă cel putin o litera mare!")
        if self.password.isalnum():
            raise Exception("Parola trebuie sa aibă cel putin un caracter special (-, /, ?, @ etc)")

    def check_passwords(self):
        if self.password != self.confirm_password:
            raise Exception("Parolele nu coincid")

    def add(self):
        self.validate_input_request()
        get_by_username = self.user_db.read(username=self.username)
        get_by_email = self.user_db.read(email=self.email)
        if get_by_email or get_by_username:
            raise Exception("Username-ul sau email-ul exista deja in baza de date!")
        self.user_db.create(self.formatting_input())

    def check_in_db(self):
        users = self.user_db.read(email=self.email)
        if not users:
            raise Exception("Nu sunteți înregistrat cu acest email!")
        user = users[0]
        if user["password"] != self.password:
            raise Exception("Parolă invalidă!")
        return True

    def formatting_input(self):
        return {
            'id': str(uuid.uuid4()),
            'username': self.username,
            'password': self.password,
            'email': self.email
        }

