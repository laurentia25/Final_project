from db.CRUD.products_crud import ProductsDb


class Cart(ProductsDb):
    products_json = []

    def add_to_cart(self, product_id):
        products_in_cart = []
        if product_id:
            products_in_cart.append(product_id)
            for product in products_in_cart:
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
                    self.products_json.append(product_json)
                print(products_in_cart)
                return self.products_json

    def clear_cart(self):
        self.products_json.clear()
        return self.products_json

    def delete_cart_product(self, prod_id):
        self.products_json.remove(prod_id)
        return self.products_json


    def create(self):
        pass

    def read(self, id=None, category=None):
        pass

    def update(self):
        pass

    def delete(self):
        pass
