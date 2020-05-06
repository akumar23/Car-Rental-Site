from flask import render_template, flash, redirect, url_for, Markup
from app import app
from app import db
from app.forms import LoginForm
from app.forms import RegistrationForm
from app.models import User
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
import requests
import json


car_info = [
    {
        "id": "100",
        "name": "Jeep",
        "img": "hummer.jpg",
        "price": 50,
        "carAmount": 20,
    },

    {
        "id": "101",
        "name": "Tesla Model Y",
        "img": "model-y.png",
        "price": 45,
        "carAmount": 25,
    },

    {
        "id": "102",
        "name": "Tesla Model 3",
        "img": "model3.png",
        "price": 45,
        "carAmount": 20,
    },

    {
        "id": "103",
        "name": "Mercedes 2025",
        "img": "mercedes.jpg",
        "price": 225,
        "carAmount": 0,
    },

    {
        "id": "104",
        "name": "Ferrari",
        "img": "ferrari.png",
        "price": 125,
        "carAmount": 3,
    },

    {
        "id": "105",
        "name": "Audi",
        "img": "audi.jpg",
        "price": 75,
        "carAmount": 5,
    },

    {
        "id": "106",
        "name": "BMW i8",
        "img": "bmwi8.jpg",
        "price": 100,
        "carAmount": 28,
    },

    {
        "id": "107",
        "name": "Audi Convertible",
        "img": "audiConvertible.jpg",
        "price": 50,
        "carAmount": 27,
    },

    {
        "id": "108",
        "name": "Audi Trail",
        "img": "audiTrail2.jpg",
        "price": 35,
        "carAmount": 45,
    },

    {
        "id": "109",
        "name": "Jaguar F Type",
        "img": "jaguarFT.jpg",
        "price": 55,
        "carAmount": 5,
    },

    {
        "id": "110",
        "name": "Blade Runner Car",
        "img": "bladeRunnerCar.png",
        "price": 235,
        "carAmount": 3,
    }
]

def listInHtml(product):
    html = ""
    image_url = url_for("static", filename=product["img"])
    car_url = url_for("car", product_id=product["id"])
    html = html + "<li>"
    html = html + '<a href="' + car_url + '">'
    html = (html + '<img src="' + image_url +
        '" al  t="' + product["name"] + '">')
    html = html + "<p>View Details</p>"
    html = html + "</a>"
    html = html + "</li>"

    return html

@app.route("/carPage")
def carPage():
    context = {"page_title": "EZPZ"}
    product_data = []
    for product in car_info:
        product_data.append(Markup(listInHtml(product)))
    context["product_data"] = Markup("".join(product_data))
    return render_template("carPage.html", **context)

@app.route("/car/<product_id>")
def car(product_id):
    context = {"page_title": "EZPZ"}
    my_product = ""
    for product in car_info:
        if product["id"] == product_id:
            my_product = product
            product["carAmount"] = product["carAmount"]-1
    context["product"] = my_product
    return render_template("car.html", **context)

@app.route("/checkout")
def checkout():
    return render_template("checkout.html")

@app.route("/receipt")
def receipt():
    context = {"page_title": "EZPZ"}
    return render_template("receipt.html", **context)

@app.route('/')
def index():
    context = {"page_title": "EZPZ"}
    counter = 0
    product_data = []
    for product in car_info:
        counter += 1
        if counter < 5:
            product_data.append(
                Markup(listInHtml(product))
            )
    context["product_data"] = Markup("".join(product_data))
    return render_template("index.html", **context)
