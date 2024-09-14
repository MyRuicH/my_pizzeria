from flask import Flask, render_template

from random import randint


app = Flask(__name__)


@app.get("/")
def index():
    hour = randint(8, 11)
    return render_template("index.html", hour=hour)


@app.get("/menu/")
def menu():
    context = {
        "price": randint(15, 31),
        "percent": randint(20, 61)
            }   
    return render_template("menu.html", **context)


@app.get("/contacts/")
def contacts():
    context = {
        "first_numbers": randint(101, 999),
        "second_numbers": randint(1001, 9999)
             }
    return render_template("contacts.html", **context)


if __name__ == "__main__":
    app.run(debug=True)
    