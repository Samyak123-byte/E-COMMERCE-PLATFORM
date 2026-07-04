from flask import Blueprint, render_template, abort, request

# ✅ MUST be at top before any @main.route
main = Blueprint('main', __name__)

# ---------------- MOCK PRODUCTS ----------------
MOCK_PRODUCTS = [
    {
        "id": 1,
        "name": "Classic T-Shirt",
        "price": 499.00,
        "description": "100% cotton comfortable wear.",
        "image": "tshirt.jpg"
    },
    {
        "id": 2,
        "name": "Running Shoes",
        "price": 2499.00,
        "description": "Lightweight shoes designed for athletes.",
        "image": "shoes.jpg"
    },
    {
        "id": 3,
        "name": "Leather Wallet",
        "price": 899.00,
        "description": "Genuine leather slim wallet.",
        "image": "wallet.jpg"
    }
]

# ---------------- ROUTES ----------------

@main.route('/')
def home():
    return render_template('index.html', products=MOCK_PRODUCTS)


@main.route('/products')
def products():
    return render_template('products.html', products=MOCK_PRODUCTS)


@main.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in MOCK_PRODUCTS if p["id"] == product_id), None)
    if not product:
        abort(404)
    return render_template('product_detail.html', product=product)


@main.route('/cart')
def cart():
    return render_template('cart.html', cart_items=[], total=0)


@main.route('/search')
def search():
    query = request.args.get('q', '')

    filtered = [
        p for p in MOCK_PRODUCTS
        if query.lower() in p["name"].lower()
        or query.lower() in p["description"].lower()
    ]

    return render_template('products.html', products=filtered)


@main.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@main.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@main.route('/profile')
def profile():
    return "Profile Page"


@main.route('/logout')
def logout():
    return "Logout Page"