from db.CRUD.interface_CRUD import CrudABC


class UsersDb(CrudABC):
    def create(self, user_details):
        sql_query = """
        INSERT INTO Users(id, username, password, email)
        VALUES(:id, :username, :password, :email);
        """
        cursor = self.connection.cursor()
        cursor.execute(
            sql_query ,
            user_details
        )
        self.connection.commit()

    def read(self, email=None, username=None):
        read_query = """
        SELECT * FROM Users
        WHERE email = ?;
        """
        cursor = self.connection.cursor()
        cursor.execute(read_query, (email,))

        users = cursor.fetchall() # returneaza o lista cu liste
        # va fi mult mai utila o lista cu dictionare
        users_json = []
        for user in users:
            users_json.append({
                "id": user[0],
                "username": user[1],
                "password": user[2],
                "email": user[3]
                }
            )

        return users_json

    def update(self):
        pass

    def delete(self):
        pass
