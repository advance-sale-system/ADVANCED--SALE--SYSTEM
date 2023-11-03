
from flask import render_template,session,request,url_for,redirect,flash
from dbservice import *
from flask_login import LoginManager, logout_user, login_user, current_user
from werkzeug.security import generate_password_hash,check_password_hash



app.secret_key="Techcamp"
login_manager = LoginManager(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))


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


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method=="POST":
        email = request.form["email"]
        password = request.form["password"]

        user=Users.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash("Welcome")
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid logins")

    return render_template("login.html")



@app.route("/products", methods=["GET","POST"])
def products():
    # reterive form data
    if request.method=="POST":
        product_name = request.form["product_name"]
        buying_price = request.form["buying_price"]
        selling_price = request.form["selling_price"]
        stock_quantity = request.form["stock_quantity"]
        # create new product instance with the form data
        new_product=Products(
            product_name=product_name,
            buying_price=buying_price,
            selling_price=selling_price,
            stock_quantity=stock_quantity
        )
        # add te new product to the database session
        db.session.add(new_product)
        # commit the changes to the database
        db.session.commit()
        flash("Product added succesfully")
        return redirect(url_for("products"))


    records=Products.query.all()
    products=[prod for prod in records]
    return render_template("products.html", products=products)


@app.route("/make-sale")
def make_sale():
    sale=Sales.query.get(id)
    # retrieve form data for the sale details
    if request.method == 'POST':
        product_id = request.form['product_id']
        quantity = request.form['quantity']
        purchase_amount = request.form['purchase_amount']
        

        # create sale detail object
        sale_detail = SaleDetails(sale_id=sale,product_id=product_id,quantity=quantity,purchase_amount=purchase_amount)
        db.session.add(sale_detail)
        db.session.commit
        flash("Sale added")
        return redirect(url_for('make_sale'))



@app.route("/sales", methods=["GET"])
def sales():
    records=Sales.query.all()
    sales=[sale for sale in records]
    return render_template("sales.html", sales=sales)


@app.route("/add-sales")
def add_sales():
     return render_template("addsale.html")


@app.route("/logout")
def logout():
    logout_user()
    flash("Logged Out")
    return redirect(url_for("login"))

if __name__== "__main__":
    app.run(debug=True)