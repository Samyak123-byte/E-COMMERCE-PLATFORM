import os
import secrets
from PIL import Image
from flask import current_app
from functools import wraps
from flask import abort
from flask_login import current_user # type: ignore


def save_picture(uploaded_file):
    """
    Save uploaded product image with a random filename.
    Resize image before saving.
    Returns the new filename.
    """

    random_hex = secrets.token_hex(8)
    _, file_ext = os.path.splitext(uploaded_file.filename)
    picture_filename = random_hex + file_ext

    picture_path = os.path.join(
        current_app.root_path,
        'static/images/products',
        picture_filename
    )

    output_size = (600, 600)

    image = Image.open(uploaded_file)
    image.thumbnail(output_size)
    image.save(picture_path)

    return picture_filename


def delete_picture(filename):
    """Delete a product image from storage."""

    if filename == "default.jpg":
        return

    picture_path = os.path.join(
        current_app.root_path,
        'static/images/products',
        filename
    )

    if os.path.exists(picture_path):
        os.remove(picture_path)


def admin_required(func):
    """
    Restrict route access to admin users only.
    Assumes User model has an 'is_admin' boolean field.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated:
            abort(401)

        if not current_user.is_admin:
            abort(403)

        return func(*args, **kwargs)

    return wrapper


def format_currency(amount):
    """
    Format currency in Indian Rupees.
    """

    return f"₹{amount:,.2f}"


def generate_order_number():
    """
    Generate a unique order number.
    Example: ORD-9F3A2B1C
    """

    return f"ORD-{secrets.token_hex(4).upper()}"


def allowed_file(filename):
    """
    Check if uploaded file extension is allowed.
    """

    allowed_extensions = {"png", "jpg", "jpeg", "gif", "webp"}

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in allowed_extensions
    )


def calculate_cart_total(cart_items):
    """
    Calculate total amount of cart.
    Expects each cart item to have:
        item.product.price
        item.quantity
    """

    total = 0

    for item in cart_items:
        total += item.product.price * item.quantity

    return total


def calculate_cart_count(cart_items):
    """
    Calculate total number of items in cart.
    """

    return sum(item.quantity for item in cart_items)