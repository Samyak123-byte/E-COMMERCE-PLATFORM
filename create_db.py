from app import app, db  # Or however you import your app and db instances

# Wrap the creation process in the application context
with app.app_context():
    print("Creating database tables...")
    db.create_all()
    print("Database tables created successfully!")
