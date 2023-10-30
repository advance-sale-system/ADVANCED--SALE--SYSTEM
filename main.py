
from flask import render_template,session,request,url_for,redirect,flash
from dbservice import *
from flask_login import LoginManager
from werkzeug.security import generate_password_hash,check_password_hash


app.secret_key="Techcamp"

@app.route("/")
def advanced_system():
    return render_template("index.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method=="POST":
        email = request.form["email"]
        password = request.form["password"]
        hashed_pass=generate_password_hash(password)
        # check email existence
        user=Users.query.filter_by(email=email).first()
        print("User")

        if user:
            print("")
            flash("Email already exist")
        else:
            new_user=Users(email=email,password=hashed_pass)
            db.session.add(new_user)
            db.session.commit()
            flash("You have succesfully registered")
            return redirect(url_for('login'))

    return render_template("register.html")


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
    records=Sales.query.all()
    sales=[sale for sale in records]
    return render_template("sales.html", sales=sales)


if __name__== "__main__":
    app.run(debug=True)