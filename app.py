"""
Entrypoint-ul in aplicatia pentru proiectul final
dezvoltata folosind framework-ul Flask
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True, port=7000)