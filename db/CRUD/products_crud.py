import json

from db.CRUD.interface_CRUD import CrudABC


class ProductsDb(CrudABC):

    def create(self):
        pass

    def read(self, id=None):
        sql_query = "SELECT * FROM Products"
        value = ''
        if id:
            sql_query += "WHERE id=?;"
            value = id
        cursor = self.connection.cursor()
        if not value:
            cursor.execute(sql_query)
        else:
            cursor.execute(sql_query, (value,))

        products = cursor.fetchall()

        products_json = []
        for product in products:
            products_json.append(
                {
                    "name": product[0],
                    "description": product[1],
                    "price": product[2],
                    "weight": product[3],
                    "available_quantity": product[4],
                    "image":product[5]
                }
            )
        return products_json

    def update(self):
        pass

    def delete(self):
        pass

    def setup_products(self, source_path):
        cursor = self.connection.cursor()
        cursor.execute(
            """
            SELECT * FROM Products;
            """
        )
        if not cursor.fetchone():
            with open(source_path, mode="r") as file:
                products = json.load(file)
                table_data = [
                    (
                        product['name'],
                        product["description"],
                        product['price'],
                        product['weight'],
                        product['available_quantity'],
                        product['image']
                    ) for product in products]
                query = """
                INSERT INTO Products (name, description, price, weight, available_quantity, image)
                VALUES (?, ?, ?, ?, ?, ?);
                """
                cursor.executemany(query, table_data)
                self.connection.commit()