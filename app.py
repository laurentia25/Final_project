"""
Entrypoint-ul in aplicatia pentru proiectul final
dezvoltata folosind framework-ul Flask
"""

from flask import Flask, render_template, request

from db.db_connection import create_database

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    # logica asociata cu metoda POST, nu e nevoie de else
    user_data = dict(request.form) #-> dictionar cu info din form
    print("===================")
    print(user_data)


if __name__ == '__main__':
    create_database()
    app.run(debug=True, port=7000)
