
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    FloatField,
    IntegerField,
    TextAreaField,
    SelectField,
    BooleanField
)
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
    NumberRange
)


# ----------------------------
# Login Form
# ----------------------------

class LoginForm(FlaskForm):

    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired()
        ]
    )

    remember = BooleanField("Remember Me")

    submit = SubmitField("Login")


# ----------------------------
# Register Form
# ----------------------------

class RegisterForm(FlaskForm):

    name = StringField(
        "Full Name",
        validators=[
            DataRequired(),
            Length(min=3, max=100)
        ]
    )

    username = StringField(
        "Username",
        validators=[
            DataRequired(),
            Length(min=3, max=30)
        ]
    )

    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email()
        ]
    )

    phone = StringField(
        "Phone Number",
        validators=[
            Length(max=20)
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=6)
        ]
    )

    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo(
                "password",
                message="Passwords must match."
            )
        ]
    )

    submit = SubmitField("Register")


# ----------------------------
# Category Form
# ----------------------------

class CategoryForm(FlaskForm):

    name = StringField(
        "Category Name",
        validators=[
            DataRequired(),
            Length(max=100)
        ]
    )

    submit = SubmitField("Save Category")


# ----------------------------
# Product Form
# ----------------------------

class ProductForm(FlaskForm):

    name = StringField(
        "Product Name",
        validators=[
            DataRequired()
        ]
    )

    description = TextAreaField(
        "Description",
        validators=[
            DataRequired()
        ]
    )

    price = FloatField(
        "Price",
        validators=[
            DataRequired(),
            NumberRange(min=0)
        ]
    )

    stock = IntegerField(
        "Stock",
        validators=[
            DataRequired(),
            NumberRange(min=0)
        ]
    )

    category_id = SelectField(
        "Category",
        coerce=int,
        validators=[
            DataRequired()
        ]
    )

    image = FileField(
        "Product Image",
        validators=[
            FileAllowed(
                ["jpg", "jpeg", "png", "gif", "webp"],
                "Images only!"
            )
        ]
    )

    submit = SubmitField("Save Product")


# ----------------------------
# Checkout Form
# ----------------------------

class CheckoutForm(FlaskForm):

    name = StringField(
        "Full Name",
        validators=[DataRequired()]
    )

    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email()
        ]
    )

    phone = StringField(
        "Phone",
        validators=[DataRequired()]
    )

    address = TextAreaField(
        "Address",
        validators=[DataRequired()]
    )

    city = StringField(
        "City",
        validators=[DataRequired()]
    )

    state = StringField(
        "State",
        validators=[DataRequired()]
    )

    zip = StringField(
        "ZIP Code",
        validators=[DataRequired()]
    )

    country = StringField(
        "Country",
        validators=[DataRequired()]
    )

    payment = SelectField(
        "Payment Method",
        choices=[
            ("cod", "Cash on Delivery"),
            ("razorpay", "Razorpay"),
            ("stripe", "Stripe")
        ]
    )

    submit = SubmitField("Place Order")


# ----------------------------
# Search Form
# ----------------------------

class SearchForm(FlaskForm):

    q = StringField("Search")

    submit = SubmitField("Search")

