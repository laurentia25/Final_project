"""
Entrypoint-ul in aplicatia pentru proiectul final
dezvoltata folosind framework-ul Flask
"""

from flask import Flask, render_template, request, redirect, session

from db.CRUD.products_crud import ProductsDb
from db.db_connection import create_database
from models.user import User

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    # logica asociata cu metoda POST, nu e nevoie de else
    user_data = dict(request.form) # -> dictionar cu info din form
    # user_obj = User(email=user_data['email'], password=user_data['password'])
    try:
        user_obj = User(**user_data)
        user_obj.check_in_db()
    except Exception as error:
        return render_template("login.html", error=f"{error}")
    return redirect('/products')


@app.route('/cart', methods=['GET'])
def get_checkout():
    return render_template('cart.html', user=session.get('user', False))


@app.route("/users")
def get_all_users():
    return render_template("sign_up.html")


@app.route("/users/add", methods=["GET", "POST"])
def add_user():
    if request.method == "GET":
        return render_template('sign_up.html')
    user_data = dict(request.form)
    try:
        user_obj = User(**user_data)
        user_obj.add()
    except Exception as error:
        return render_template("sign_up.html", error=f'{error}')
    return redirect('/products')


@app.route('/products', methods=['GET'])
def get_all_products():
    products_object = ProductsDb()
    products = products_object.read()
    return render_template("products.html", products=products, user=session.get("user", False))


@app.route('/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    products_object = ProductsDb()
    products = products_object.read(id=product_id)
    return render_template("product_zoom.html", products=products[0], user=session.get("user", False))


@app.route('/products/<category>', methods=['GET'])
def get_product_by_category(category):
    products_object = ProductsDb()
    products = products_object.read(category=category)
    return render_template('products.html', products=products, user=session.get("user", False))


if __name__ == '__main__':
    create_database()
    products_crud = ProductsDb()
    products_crud.setup_products('./db/products_setup.json')
    app.run(debug=True, port=7000)
