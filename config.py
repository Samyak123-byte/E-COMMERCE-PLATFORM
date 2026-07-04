
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


class Config:
    # Flask Configuration
    SECRET_KEY = os.getenv("SECRET_KEY", "change-this-secret-key")

    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///ecommerce.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Upload Folder
    UPLOAD_FOLDER = os.path.join(
        "static",
        "images",
        "products"
    )

    # Maximum Upload Size (16 MB)
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    # Allowed Image Extensions
    ALLOWED_EXTENSIONS = {
        "png",
        "jpg",
        "jpeg",
        "gif",
        "webp"
    }

    # Flask Session
    SESSION_PERMANENT = False

    # Flask-WTF
    WTF_CSRF_ENABLED = True

    # Remember Me Cookie
    REMEMBER_COOKIE_DURATION = 60 * 60 * 24 * 7

    # Mail Configuration
    MAIL_SERVER = os.getenv("MAIL_SERVER", "smtp.gmail.com")
    MAIL_PORT = int(os.getenv("MAIL_PORT", 587))
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_USERNAME")

    # Razorpay
    RAZORPAY_KEY_ID = os.getenv("RAZORPAY_KEY_ID")
    RAZORPAY_KEY_SECRET = os.getenv("RAZORPAY_KEY_SECRET")

    # Stripe
    STRIPE_PUBLIC_KEY = os.getenv("STRIPE_PUBLIC_KEY")
    STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
