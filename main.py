
from flask import render_template,session,request,url_for,redirect
from dbservice import *


app.secret_key="Techcamp"

@app.route("/")
def advanced_system():
    return render_template("index.html")


@app.route("/register")
def register():
    return redirect(url_for("login"))


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/login")
def login():
    return redirect(url_for("dashboard"))


@app.route("/products")
def products():
    records=Products.query.all()
    products=[prod for prod in records]
    return render_template("products.html", products=products)


@app.route("/sales")
def sales():
    return render_template("sales.html")


if __name__== "__main__":
    app.run()