from db.CRUD.products_crud import ProductsDb


class Cart(ProductsDb):

    def add_to_cart(self, product_id):
        products_to_cart = []
        if product_id:
            products_to_cart.append(product_id)
            products_json = []
            print(products_to_cart)
            for product in products_to_cart:
                sql_query = "SELECT * FROM Products WHERE id=?;"
                cursor = self.connection.cursor()
                cursor.execute(sql_query, (product, ))
                product_to_cart = cursor.fetchone()
                if product_to_cart:
                    product_json = {
                         "id": product_to_cart[0],
                         "name": product_to_cart[1],
                         "price": product_to_cart[2],
                         "image": product_to_cart[6]
                          }
                    products_json.append(product_json)
            print(products_json)
            return products_json

    def create(self):
        pass

    def read(self, id=None, category=None):
        pass

    def update(self):
        pass

    def delete(self):
        pass
