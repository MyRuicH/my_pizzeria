from flask import Flask, render_template

from random import randint


app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/menu/")
def menu():
    price = randint(15, 30)
    return render_template("menu.html", price=price)


@app.get("/contacts/")
def contacts():
    return render_template("contacts.html")


if __name__ == "__main__":
    app.run(debug=True)
    