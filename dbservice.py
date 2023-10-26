from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import DateTime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:2345@localhost:5432/duka"

db = SQLAlchemy(app)

class Products (db.model):
    __tablename__ = 'products'
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(255), nullable=False)
    buying_price = db.Column(db.Numeric(precision=15, scale=2), nullable=False)
    selling_price = db.Column(db.Numeric(precision=15, scale=2))
    stock_quantity = db.Column(db.Numeric(precision=15, scale=2))
    sales_details = db.relationship("SalesDetails", back_ref="products")


class Customers (db.model):
    __tablename__ = 'customers'
    customer_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255))
    phone_no = db.Column(db.String(13), nullable=False)
    email = db.Column(db.String(255))
    sales = db.relationship("Sales", back_ref="customers")
    payments = db.relationship("Payments", back_ref="customers")



class Employees(db.model):
    __tablename__ = 'employees'
    employee_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False )
    email = db.Column(db.String(255))
    contact = db.Column(db.Srting(13), nullable=False)
    position = db.Column(db.Srting(255), nullable=False)
    users = db.relationship("Users", back_ref="employees")


class Users(db.model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee_id'))
    password = db.Column(db.String(255), nullable=False)
    user_email = db.Column(db.String(255), nullable=False, unique=True)
    sales = db.realtionship("Sales", back_ref="users")


class Sales(db.Model):
    __tablename__ = 'sales'
    sale_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user_id'))
    total_amount = db.Column(db.Numeric(precision=15, scale=2))
    created_at = db.Column(DateTime, default=db.func.current_timestamp())
    sales_details = db.relationship("SalesDetails", back_ref="sales")
    payments = db.relationship("Payments", back_ref="sales")

class SaleDetails(db.model):
    __tablename__ = 'sale_details'
    id = db.Column(db.Integer, primary_key=True)
    sale_id = db.Column(db.Integer, db.ForeignKey('sale_id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product_id'))
    quantity = db.Column(db.Numeric(precision=15, scale=2))
    purchase_amount = db.Coulmn(db.Numeric(precision=15, scale=2))

class Payments(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True)
    sale_id = db.Column(db.Integer, db.ForeignKey('sale_id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer_id'))
    payment_method = db.Column(db.String(255))
    amount = db.Column(db.Numeric(precision=15, scale=2))







