from dbservice import Products, Payments,Employees,SaleDetails,Sales,Customers,Users
from flask import Flask,render_template,session,request,url_for,redirect

app= Flask(__name__)
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
    prods=Products.query.all()
    print(prods)
    return render_template("products.html")

@app.route("/sales")
def sales():
    return render_template("sales.html")
# if __name__== "__main__":
#     app.run()