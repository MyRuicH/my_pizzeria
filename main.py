from flask import Flask, render_template

import random


app = Flask(__name__)


@app.get("/")
def index():
    hour = random.randint(8, 11)
    return render_template("index.html", hour=hour)


@app.get("/menu/")
def menu():
    price = random.randint(15, 31)
    percent = random.randint(20, 61)
    return render_template("menu.html", price=price, percent=percent)


@app.get("/contacts/")
def contacts():
    return render_template("contacts.html")


if __name__ == "__main__":
    app.run(debug=True)
    