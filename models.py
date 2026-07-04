
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


# -----------------------------
# User Model
# -----------------------------

class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    username = db.Column(db.String(50), unique=True, nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    phone = db.Column(db.String(20))

    password_hash = db.Column(db.String(255), nullable=False)

    is_admin = db.Column(db.Boolean, default=False)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    orders = db.relationship(
        "Order",
        backref="user",
        lazy=True,
        cascade="all, delete"
    )

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(
            self.password_hash,
            password
        )

    def __repr__(self):
        return f"<User {self.username}>"


# -----------------------------
# Category Model
# -----------------------------

class Category(db.Model):

    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    products = db.relationship(
        "Product",
        backref="category",
        lazy=True,
        cascade="all, delete"
    )

    def __repr__(self):
        return self.name


# -----------------------------
# Product Model
# -----------------------------

class Product(db.Model):

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(
        db.String(200),
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=False
    )

    price = db.Column(
        db.Float,
        nullable=False
    )

    stock = db.Column(
        db.Integer,
        default=0
    )

    image = db.Column(
        db.String(255),
        default="default.png"
    )

    category_id = db.Column(
        db.Integer,
        db.ForeignKey("categories.id"),
        nullable=False
    )

    order_items = db.relationship(
        "OrderItem",
        backref="product",
        lazy=True
    )

    def __repr__(self):
        return self.name


# -----------------------------
# Order Model
# -----------------------------

class Order(db.Model):

    __tablename__ = "orders"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    total = db.Column(
        db.Float,
        nullable=False
    )

    payment_method = db.Column(
        db.String(50),
        default="Cash on Delivery"
    )

    status = db.Column(
        db.String(50),
        default="Pending"
    )

    address = db.Column(db.Text)

    city = db.Column(db.String(100))

    state = db.Column(db.String(100))

    zip_code = db.Column(db.String(20))

    country = db.Column(db.String(100))

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    items = db.relationship(
        "OrderItem",
        backref="order",
        lazy=True,
        cascade="all, delete"
    )

    def __repr__(self):
        return f"Order #{self.id}"


# -----------------------------
# Order Item Model
# -----------------------------

class OrderItem(db.Model):

    __tablename__ = "order_items"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    order_id = db.Column(
        db.Integer,
        db.ForeignKey("orders.id"),
        nullable=False
    )

    product_id = db.Column(
        db.Integer,
        db.ForeignKey("products.id"),
        nullable=False
    )

    quantity = db.Column(
        db.Integer,
        default=1
    )

    price = db.Column(
        db.Float,
        nullable=False
    )

    def subtotal(self):
        return self.price * self.quantity

    def __repr__(self):
        return f"OrderItem {self.id}"

