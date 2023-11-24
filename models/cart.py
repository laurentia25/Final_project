from db.CRUD.products_crud import ProductsDb


class Cart:

    def __init__(self,
                 products_to_cart=None,
                 product_to_buy=None
                 ):

        self.products_to_cart = products_to_cart
        self.product_to_buy = product_to_buy
        self.products_db = ProductsDb()

    def add_to_cart(self):
        products_to_cart = []

        if self.product_to_buy:
            products_to_cart.append(self.product_to_buy)
            return self.products_to_cart
