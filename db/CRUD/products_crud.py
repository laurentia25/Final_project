import json

from db.CRUD.interface_CRUD import CrudABC


class ProductsDb(CrudABC):
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
                        product['category'],
                        product['available_quantity'],
                        product['image']
                    ) for product in products]
                query = """
                INSERT INTO Products (name, description, price, category, available_quantity, image)
                VALUES (?, ?, ?, ?, ?, ?);
                """
                cursor.executemany(query, table_data)
                self.connection.commit()

    def create(self):
        pass

    def read(self, id=None, category=None):
        sql_query = "SELECT * FROM Products"
        value = ''
        if id:
            sql_query += " WHERE id=?;"
            value = id
        if category:
            sql_query += " WHERE category=?;"
            value = category
        cursor = self.connection.cursor()
        if not value:
            cursor.execute(sql_query)
        else:
            print("SQL Query:", sql_query)
            cursor.execute(sql_query, (value,))

        products = cursor.fetchall()

        products_json = []
        for product in products:
            products_json.append(
                {
                    "id": product[0],
                    "name": product[1],
                    "price": product[2],
                    "category": product[3],
                    "description": product[4],
                    "available_quantity": product[5],
                    "image": product[6]
                }
            )
        return products_json

    def update(self):
        pass

    def delete(self):
        pass

