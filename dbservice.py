from flask_sqlalchemy import SQLAlchemy
from flask import Flask
# from sqlalchemy import Column, Integer, ForeignKey, String, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy import DateTime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:2345@localhost:5432/duka"
db = SQLAlchemy(app)

# class Products(db.Model):
#     __tablename__ = 'products'
#     product_id = db.Column(db.Integer, primary_key=True)
#     product_name = db.Column(db.String(255), nullable=False)
#     buying_price = db.Column(db.Numeric(precision=15, scale=2), nullable=False)
#     selling_price = db.Column(db.Numeric(precision=15, scale=2))
#     stock_quantity = db.Column(db.Numeric(precision=15, scale=2))
#     sales_details = relationship("SaleDetails", back_populates="product") 


# class SaleDetails(db.Model):
#     __tablename__ = 'sale_details'
#     id = db.Column(db.Integer, primary_key=True)
#     sale_id = db.Column(db.Integer, db.ForeignKey('sales.sale_id'))
#     product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'))
#     quantity = db.Column(db.Numeric(precision=15, scale=2))
#     purchase_amount = db.Column(db.Numeric(precision=15, scale=2))
#     product = relationship("Products", back_populates="sales_details") 
#     sales = relationship("Sales", back_populates="sale_details") 


# class Customers (db.Model):
#     __tablename__ = 'customers'
#     customer_id = db.Column(db.Integer, primary_key=True)
#     full_name = db.Column(db.String(255))
#     phone_no = db.Column(db.String(13), nullable=False)
#     email = db.Column(db.String(255))
#     sales = relationship("Sales", back_populates="customers") 
#     payments = relationship("Payments", back_populates="customers") 


# class Employees(db.Model):
#     __tablename__ = 'employees'
#     employee_id = db.Column(db.Integer, primary_key=True)
#     full_name = db.Column(db.String(255), nullable=False)
#     email = db.Column(db.String(255))
#     contact = db.Column(db.String(13), nullable=False)
#     position = db.Column(db.String(255), nullable=False)
#     # users = relationship("Users", back_populates="employees") 


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    # sales = relationship("Sales", back_populates="users") 
    # employees = relationship("Employees", back_populates="users") 
    

# class Sales(db.Model):
#     __tablename__ = 'sales'
#     sale_id = db.Column(db.Integer, primary_key=True)
#     customer_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'))
#     # user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
#     # i think payement id is not here
#     total_amount = db.Column(db.Numeric(precision=15, scale=2))
#     created_at = db.Column(DateTime, default=db.func.current_timestamp())
#     sale_details = relationship("SaleDetails", back_populates="sales") 
#     # users = relationship("Users", back_populates="sales") 
#     customers = relationship("Customers", back_populates="sales") 
    

# class Payments(db.Model):
#     __tablename__ = 'payments'
#     id = db.Column(db.Integer, primary_key=True)
#     sale_id = db.Column(db.Integer, db.ForeignKey('sales.sale_id'))
#     customer_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'))
#     payment_method = db.Column(db.String(255))
#     amount = db.Column(db.Numeric(precision=15, scale=2))
#     customers = relationship("Customers", back_populates="payments") 






